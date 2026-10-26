import platform
import shutil
import subprocess
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

DOWNLOAD_URL = "https://github.com/tailwindlabs/tailwindcss/releases"


class Command(BaseCommand):
    help = "Compile Tailwind CSS via the standalone Tailwind CLI"

    def add_arguments(self, parser):
        subparsers = parser.add_subparsers(dest="subcommand", required=True)
        subparsers.add_parser("build", help="Compile a minified production stylesheet")
        subparsers.add_parser("start", help="Watch templates and rebuild CSS on change")

    def handle(self, *args, **options):
        base_dir = settings.BASE_DIR
        cmd = [
            str(self._find_binary()),
            "-i", str(base_dir / "static/css/input.css"),
            "-o", str(base_dir / "static/css/output.css"),
        ]
        if options["subcommand"] == "build":
            cmd.append("--minify")
        else:
            cmd.append("--watch")

        self.stdout.write(f"Running: {' '.join(cmd)}")
        try:
            subprocess.run(cmd, check=True)
        except KeyboardInterrupt:
            pass  # clean exit from watch mode
        except subprocess.CalledProcessError as e:
            raise CommandError(f"Tailwind CLI exited with status {e.returncode}")

    def _find_binary(self):
        base_dir = settings.BASE_DIR
        name = "tailwindcss.exe" if platform.system() == "Windows" else "tailwindcss"
        candidates = [base_dir / name, base_dir / "tailwindcss", shutil.which("tailwindcss")]
        for candidate in candidates:
            if candidate and Path(candidate).is_file():
                return candidate
        raise CommandError(
            f"Tailwind CLI not found. Download the standalone binary for your "
            f"platform from {DOWNLOAD_URL} and place it in the project root as "
            f"'{name}' (or install it on your PATH)."
        )
