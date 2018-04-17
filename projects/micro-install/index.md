---
layout: page
title: micro_install
permalink: /projects/micro-install
breadcrumb: micro_install
tags:
- mkmatter
- ruby
- gem
- rubygems
- micro
- text-editor
page_links:
  'micro_install on RubyGems.org': https://rubygems.org/gems/micro_install
  GitHub: https://github.com/IotaSpencer/micro_install
  micro: https://github.com/zyedidia/micro
  getmic.ro: https://github.com/benweissmann/getmic.ro
---
# micro_install

## About

micro_install is a ruby gem ported from [@benweissmann](https://github.com/benweissmann)'s 'curl'able script hosted at https://getmic.ro, and micro is developed and owned by [@zyedidia](https://github.com/zyedidia)

micro_install is used as an ruby port to benweissmann's [https://getmic.ro](https://getmic.ro) but packaged as a gem.
It installs [@zyedidia](https://github.com/zyedidia)'s micro, a terminal text editor.
The gem itself is also installed when [mkmatter](https://iotaspencer.me/projects/mkmatter) is installed.
If installed by running `micro-install`{:.highlight} then mkmatter uses `micro`{:.highlight} by default when it asks to open an editor.

micro_install is either installed via `gem install micro_install`{:.highlight} or can be cloned
 and installed using a combination of `bundle install`{:.highlight}

## Usage

To use micro_install, all you should have to do is

```shell
$ bundle exec micro-install [options]
$ micro-install [options]
# ...
# Installer runs
```