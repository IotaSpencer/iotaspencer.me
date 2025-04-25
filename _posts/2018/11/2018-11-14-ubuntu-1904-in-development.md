---
layout: post
title: Ubuntu 19.04 in Development
author: IotaSpencer
description: Ubuntu 19.04, the latest non-lts stable is under development
categories:
- Ubuntu
- Linux
- Release
tags:
- ubuntu
- ubuntu 19.04
- linux
- kubuntu
- kubuntu 19.04
- lubuntu
- lubuntu 19.04
- xubuntu
- xubuntu 19.04
- ubuntu mate
- ubuntu mate 19.04
date: '2018-11-14 20:41:17 -0500'
scrolllist:
  - group: Python
    text: >
        Ubuntu 19.04 will be shipped with Python 3.7 as default on install.
        <br><br>
        Due to Python 2.x impending EOL date, its pertinent that any python
        software is rectified to align with 3.7's conventions.  In my own
        experience I see the print ... vs print() and the switch between str
        being a base string in 2.7 and a unicode string by default in 3.7
        coming into play. That is of course if the people making such libraries
        are still keeping their library maintained.

  - group: System (not systemd related)
    text: >
        Part of Ubuntu 19.04 big changes is the departure from separate
        directories for `/bin`{:.highlight} vs `/usr/bin`{:.highlight} which is set to also mean `/lib`{:.highlight} vs `/usr/lib`{:.highlight}
        and `/sbin/`{:.highlight} vs `/usr/sbin`{:.highlight} will also be symlinked to their '/usr' based directory.
  - group: Technical
    text: >
        To complement the version, other prominent and needed libraries will be updated to their newest stable/stable-ish versions.

        * GSConnect (Tried for 18.10 but didn't materialize)

        * GCC 8.x stable

        * Linux Kernel 4.21 (Seemingly could end up being versioned 5.0)

        * Mesa 19.0

        * Gnome 3.32 (For flavors that use it)
---
{::options parse_block_html="true" /}

As of **13/Nov/2018** Ubuntu's core, versioned 19.04, and code-named 'Disco Dingo'
is currently under development. And set to release April 2019, as per rolling
release date conventions.

A few of the coming features and other changes are as follows

{% for item in page.scrolllist %}
<h4>{{item.group}}</h4>
<p>{{item.text}}</p>
{% endfor %}
