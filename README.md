# Team Firefly Discord Embeds

This is a small script that sends embed objects to the Team Firefly Discord server.

- Reads embed data from "embeds.json" file
- Sends new embeds to the server channel ids
- [Roadmap](https://github.com/jeffhentschel/team-firefly-discord-embeds/issues)

## Table of Contents

- [Setup](#setup)
- [Requirements](#requirements)
- [Usage](#usage)

## Setup

The "embeds.json" file should follow the following syntax:

```js
 [
    // A category (channel) where embeds will be posted.
    {
        // (str) category type (unused)
        "type": "Books",

        // (int) channel id where embeds will be sent
        "channel": 0, // int representing the channel id,

        // data in the embed message
        "embeds": [
            {
                // (int) optional. If present this embed will be ignored.
                // If null then the embed will be sent again.
                // (updates not supported at this time.)
                "id": 0,

                // (str) embed title
                "title": "Some Title",

                // (str) optional embed author
                "author": "Some Author",

                // (str) embed description
                "description": "Description of the item.",

                // (str url) embed link
                "link": "https://example.com/",

                // (str img url) optional embed thumbnail link (jpg or png)
                "thumbnail": "Embed Thumbnail Link (should be jpg or png)",

                // optional fields with name and value strings
                "fields": [
                    { "name": "field name", "value": "field value" },
                    ...
                ]
            },
            ...
        ]
    },
    ...
]
```

## Requirements

```sh
python3 -m pip install discord
```

## Usage

Set up your environment variable to hold your discord key. You will need to set one up on the Discord developer portal.

```sh
export DISCORD_KEY=key
```

Run the script to send all embeds to Discord.

```sh
python3 embeds.py
```
