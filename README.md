# Github Release Cleanup Tool

Quick and dirty script to ease the pain of deleting Releases.

## Installation

```
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Usage

Example usage:

```
(venv) $ ./grct/grct.py 'https://github.com/repos/cgspeck/grct' 'USERNAME:PERSONAL_ACCESS_TOKEN'
```

See [here](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token) for directions on creating a Personal Access Token.

Note that this tool does not deal with paging yet, so you may have to run it a few times to do your cleanup.

## License

Github Release Cleanup Tool Copyright (C) 2020 Chris Speck

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

See [COPYING](./COPYING) for more details.
