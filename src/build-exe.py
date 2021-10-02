# coding=utf-8
""" Script for building the compiler as an executable """
try:
    import json
    from pathlib import Path
    from typing import List
    import PyInstaller.__main__
    from distutils.dir_util import copy_tree
    import pkg_resources
    import shutil
    import os
except ImportError as e:
    raise RuntimeError(
        "Failed to locate module. Please install using 'python -m pip "
        "install <module>'"
    ) from e

def resolve_base_path() -> Path:
    """ Resolves the base path """
    p: Path = Path(os.getcwd()).resolve()
    if os.path.exists(p / "src"):
        return p
    elif p.name == "src":
        p = p.parent
    else:
        raise RuntimeError(
            "Failed to resolve base path. "
            "Use as workdir either root or ./src"
        )

    return p.resolve()


def resolve_origin_path(output_type: str) -> Path:
    """ Resolves the origin path of pyinstaller """
    p: Path = Path(os.getcwd()).resolve()
    if os.path.exists(_ := p / "src" / output_type):
        p = _
    elif os.path.exists(_ := p / output_type):
        p = _
    else:
        raise RuntimeError(
            "Failed to resolve origin path. "
            "Use as workdir either root or ./src"
        )

    return (p / "parac").resolve()


BASE_PATH: Path = resolve_base_path()
DIST_PATH: Path = BASE_PATH / "dist"
BUILD_PATH: Path = BASE_PATH / "build"
PBL_PATH: Path = BASE_PATH / "src" / "lib"
EXAMPLE_PATH: Path = BASE_PATH / "examples"

# get entry path for the compiler
entry_path: Path = pkg_resources.resource_filename(__name__, "entry_cli.py")
icon_path: Path = BASE_PATH / "img" / "parac.ico"

required: List[Path] = [
    BASE_PATH / "img" / "parac.ico",
    BASE_PATH / "img" / "parac-banner.png",
    BASE_PATH / "img" / "parac.png",
    BASE_PATH / "CHANGELOG.md",
    BASE_PATH / "LICENSE",
    BASE_PATH / "USAGE-README.md"
]

with open(
        BASE_PATH / "src" / "INSTALL_AVOID_MODULES.txt", "r", encoding='utf-8'
) as file:
    AVOID_MODULES: List[str] = list(
        i.removesuffix('\n') for i in file.readlines()
    )
    _ = []
    for i in AVOID_MODULES:
        _.append("--exclude-module")
        _.append(i)
    AVOID_MODULES = _

for i in (DIST_PATH, BUILD_PATH):
    if not os.path.exists(str(i.resolve())):
        os.makedirs(str(i.resolve()), exist_ok=True)

run_config = [
    entry_path,
    "--log-level",
    "DEBUG",
    "--name",
    "parac",
    "--icon",
    str(icon_path.resolve()),
    *AVOID_MODULES,
]


def create_default_config(dest_dir: Path) -> None:
    """ Creates the default config file """
    with open(dest_dir / "compiler-config.json", "w+") as f:
        from parac import const
        f.write(json.dumps(const.DEFAULT_CONFIG, indent=4))


def create_parac_modules(output_type: str) -> None:
    """ Creates the required parac modules for the compiler """
    origin = resolve_origin_path(output_type)
    if os.path.exists(_ := BASE_PATH / "tmp"):
        try:
            os.rmdir(_)
        except Exception:
            raise RuntimeError("./tmp folder already exists")
    os.mkdir(_)

    shutil.move(str(origin), _ := str((_ / output_type).resolve()))
    origin = Path(_).resolve()

    destination = (BASE_PATH / output_type / "parac").resolve()

    if os.path.exists(destination):
        shutil.rmtree(str(destination))

    bin_path: Path = (destination / "bin").resolve()
    lib_path: Path = (destination / "lib").resolve()
    avoid = ["bin", "lib"]

    os.makedirs(str(bin_path), exist_ok=True)
    os.makedirs(str(lib_path), exist_ok=True)

    # All items are going to be copied to the bin path, since the output of
    # pyinstaller will already contain the binary as needed, so the rest of the
    # items will be from the Para-C module and managed by us
    for entry in os.scandir(origin):
        entry: os.DirEntry
        # Avoid directories that are in avoid
        if not (entry.name in avoid and entry.is_dir()):
            shutil.move(entry.path, bin_path)

    for entry in os.scandir(PBL_PATH):
        entry: os.DirEntry
        if entry.is_dir():
            copy_tree(entry.path, str((lib_path / entry.name).resolve()))
        else:
            shutil.copy(entry.path, lib_path)

    for entry in required:
        entry: Path
        shutil.copy(str(entry.resolve()), destination)

    shutil.copy(
        BASE_PATH / "README.md", destination / "PROJECT-DESCRIPTION.md"
    )
    copy_tree(
        str(EXAMPLE_PATH.resolve()),
        str((destination / "examples").resolve())
    )

    create_default_config(destination)
    # Remove automatically generated folder by pyinstaller
    shutil.rmtree(origin.parent)  # tmp


if __name__ == "__main__":
    PyInstaller.__main__.run(run_config)
    create_parac_modules("dist")
    create_parac_modules("build")
