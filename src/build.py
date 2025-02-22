from os import system
from pathlib import Path


def build_ui() -> None:
    src_directory = Path(__file__).parent
    windows_directory = src_directory / 'windows'
    ui_files = windows_directory.glob('*.ui')
    for ui_file_path in ui_files:
        system(f'pyuic6 "{ui_file_path}" -o "{ui_file_path.parent}/{ui_file_path.stem}_ui.py"')


if __name__ == '__main__':
    build_ui()
