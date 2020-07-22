#! /usr/bin/env python
import inquirer
import requests

from dataclasses import dataclass
import sys

@dataclass
class Release:
    """Class for keeping track of a Github Release."""
    name: str
    tag_name: str
    release_id: int

    @property
    def display_name(self) -> str:
        if self.name == None:
            return self.tag_name

        return self.name


print("""
Github Release Cleanup Tool  Copyright (C) 2020  Chris Speck

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
""")

args=sys.argv
if len(args) != 3:
    print(f"""

Usage: {args[0]} 'PATH_TO_REPO' 'USER:GITHUB_TOKEN'

e.g. {args[0]} 'https://github.com/repos/cgspeck/brewtarget' 'chrisbot:$GITHUB_TOKEN'
""")
    sys.exit(1)

repo_url = args[1]
owner = repo_url.split('/')[4]
repo = repo_url.split('/')[5]

user_args = args[2]
user = user_args.split(':')[0]
token=user_args.split(':')[1]

list_url = f"https://api.github.com/repos/{owner}/{repo}/releases"

print(f"Fetching {list_url}")
releases_json = requests.get(list_url, auth=(user, token)).json()

releases = []

for json_record in releases_json:
    releases.append(Release(json_record["name"], json_record["tag_name"], json_record["id"]))

if len(releases) == 0:
    print("No releases found, nothing to do!")
    sys.exit()

release_dict = [{'name':r.name} for r in releases]

questions = [
    inquirer.Checkbox(
        'releases',
        message='Select releases to delete',
        choices=releases,
    ),
]

answers = inquirer.prompt(questions)

selected_releases = answers['releases']

if len(selected_releases) == 0:
    print("No releases selected")
    sys.exit()

for selected_release in selected_releases:
    print(f"Deleting release {selected_release.display_name}")
    delete_url = f"https://api.github.com/repos/{owner}/{repo}/releases/{selected_release.release_id}"
    requests.delete(delete_url, auth=(user, token)).raise_for_status()
