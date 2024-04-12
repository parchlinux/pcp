import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

archs = (Path("x86_64"),)

base_url = "https://raw.githubusercontent.com/parchlinux/pcp/main/{arch}/{package}"


def main():
    # root README content
    README_text = "# PCP: Parch Community Packages\n\n"

    for arch in archs:
        # add current arch to root README.md
        logging.info("Generating for arch: %s", arch)
        README_text += f"- [{arch}]({arch})\n"

        # this arch README.md content body
        archs_text = "[../](..)\n\n"
        # get packages list
        packages = sorted(tuple(arch.glob("*.zst")))
        # add packages link
        for package in packages:
            logging.info("Generating for package: %s", package)
            _package_url = base_url.format(arch=arch, package=package.name)
            archs_text += "- [{name}]({url})\n".format(
                name=package.name.split(".")[0],
                url=_package_url,
            )
        # create README file for this arch
        with open(arch / "README.md", "w") as f:
            f.write(archs_text)
    # create root README.md file
    with open("README.md", "w") as f:
        f.write(README_text)


if __name__ == "__main__":
    main()
