#!/user/bin/env python3

import xml.etree.ElementTree as ET
import sys

class Host:
    data = None
    output = None
    height = 5
    top = 0
    right = 0
    indent = 5
    line_height = 18

    def __init__(self, host_data, top, right) -> None:
        self.data = host_data
        self.top = top
        self.right = right
        self.gen_output()

    def gen_output(self):
        # Ignore downed hosts
        if self.data.find("status").get("state") == "down":
            self.output = ""
            return

        self.output = '<text x="{x}px" y="{y}px" font-size="{fs}px">\n'.format(
            x=self.right, y=self.top, fs=self.line_height * 0.8
        )

        # Output will always contian the first 3 lines
        self.inc_height(3)
        # Get the host's IP
        for address in self.data.findall("address"):
            if address.get("addrtype") == "ipv4" or address.get("addrtype") == "ipv6":
                self.bold_line(address.get("addr"))

        # Get the operating system
        os = ""
        try:
            os = self.data.find("os").find("osmatch").get("name")
        except:
            os = "Unknown OS"
        self.norm_line(os)

        # List ports / services
        self.bold_line("Open ports:")
        num_ports = 0
        self.indent = 20
        if self.data.find("ports") != None:
            for port in self.data.find("ports"):
                if port.tag == "port":
                    port_data = port.get("portid") + "/" + port.get("protocol") + " | "
                    if port.find("service").get("product") is not None:
                        port_data += port.find("service").get("product")
                    else:
                        port_data += port.find("service").get("name")
                    self.norm_line(port_data)
                    self.inc_height(1)
                    num_ports += 1
        # Report if no ports
        if num_ports == 0:
            self.norm_line("No ports")
            self.inc_height(1)

        self.output += "</text>\n"
        self.output += '<rect x="{x}" y="{y}" width="40em" height="{height}" fill-opacity="0" stroke="#000" stroke-width="3px" />\n'.format(
            x=self.right, y=self.top, height=self.height
        )

    def bold_line(self, text):
        self.output += (
            '<tspan x="{}px" dy="1.2em" font-weight="bold">\n{}\n</tspan>\n'.format(
                self.right + self.indent, text
            )
        )

    def norm_line(self, text):
        self.output += '<tspan x="{}px" dy="1.2em">\n{}</tspan>\n'.format(
            self.right + self.indent, text
        )

    def inc_height(self, num_lines=1):
        self.height += num_lines * self.line_height


class Subnet:
    data = None
    output = ""
    height = 0
    top = 0
    right = 0
    indent = 50
    host_gap = 20
    host_depth = 100
    font_size = 20

    def __init__(self, filename, top, right) -> None:
        self.data = ET.parse(filename)
        self.top = top
        self.right = right
        self.host_depth += self.right
        self.gen_output()

    def gen_output(self):
        self.add_net_name()
        self.right += self.indent
        self.top += self.host_gap
        last_host_height = 0
        for host in self.data.findall("host"):
            host_obj = Host(host, self.height + self.top, self.host_depth)
            if host_obj.output != "":
                self.add_host_line()
                self.output += host_obj.output
                self.height += host_obj.height + self.host_gap
                last_host_height = host_obj.height
        self.add_vertical_line(last_host_height)

    def add_host_line(self):
        self.output += '<line x1="{left}px" x2="{right}px" y1="{height}px" y2="{height}px" stroke="#000" stroke-width="3px"/>\n'.format(
            left=self.right, right=self.host_depth, height=self.height + self.top + 20
        )

    def add_vertical_line(self, last_host_height):
        self.output += '<line x1="{right}px" x2="{right}px" y1="{top}px" y2="{bottom}px" stroke="#000" stroke-width="3px"/>\n'.format(
            right=self.right,
            top=self.top - self.host_gap + 5,
            bottom=self.top + self.height - last_host_height,
        )

    def add_net_name(self):
        nmap = self.data.getroot()
        network = nmap.get("args").split()[-1]
        self.output += (
            '<text x="{right}px" y="{top}px" font-size="{fs}px">{text}</text>\n'.format(
                right=self.right, top=self.top, fs=self.font_size, text=network
            )
        )


class NmapTree:
    filenames = []
    output = ""
    height = 0
    top = 20
    right = 20
    indent = 20
    net_gap = 50
    net_depth = 100
    font_size = 20

    def __init__(self) -> None:
        self.net_depth += self.right
        self.parse_args()
        self.gen_output()
        self.write_to_file()

    def gen_output(self):
        self.add_internet()
        self.right += self.indent
        self.top += self.net_gap
        last_net_height = 0
        for subnet in self.filenames:
            self.add_net_line()
            net_obj = Subnet(subnet, self.height + self.top, self.net_depth)
            self.output += net_obj.output
            self.height += net_obj.height + self.net_gap
            last_net_height = net_obj.height
        self.add_vertical_line(last_net_height)

    def parse_args(self):
        if len(sys.argv) < 2:
            print("Requires input filenames: nmap2svg <filename ...>")
            sys.exit(1)
        for filename in sys.argv[1:]:
            self.filenames.append(filename)

    def add_net_line(self):
        self.output += '<line x1="{left}px" x2="{right}px" y1="{height}px" y2="{height}px" stroke="#000" stroke-width="3px"/>\n'.format(
            left=self.right,
            right=self.net_depth,
            height=self.height + self.top - self.font_size / 4,
        )

    def add_vertical_line(self, last_net_height):
        self.output += '<line x1="{right}px" x2="{right}px" y1="{top}px" y2="{bottom}px" stroke="#000" stroke-width="3px"/>\n'.format(
            right=self.right,
            top=self.top - self.net_gap + 5,
            bottom=self.top
            + self.height
            - last_net_height
            - self.net_gap
            - self.font_size / 4,
        )

    def add_internet(self):
        self.output += (
            '<text x="{right}px" y="{top}px" font-size="{fs}px">{text}</text>\n'.format(
                right=self.right, top=self.top, fs=self.font_size, text="Internet"
            )
        )

    def write_to_file(self):
        f = open("nmap_scan.svg", "w")
        f.write(
            '<svg width="{width}px" height="{height}px">{body}</svg>'.format(
                width=900, height=self.top + self.height + 20, body=self.output
            )
        )
        f.close


if __name__ == "__main__":
    NmapTree()
