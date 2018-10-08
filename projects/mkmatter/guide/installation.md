---
layout: page
title: Installation
breadcrumb: Installation
categories:
- Jekyll
- mkmatter
- Installation
tags:
- mkmatter
- installation
date: '2018-03-04 06:52:40 -0500'
---
{::options parse_block_html="true" /}
<div class="float-right card bg-dark ml-4 mr-2">

# Contents
{:.no_toc .mx-auto}

* TOC
{:toc class="well bg-dark d-inline-block pr-3 py-2"}
</div>

<div>

# Installation
To install 'mkmatter', do the following.

<dl>
  <dt>Note</dt>
  <dd>
  If you decide to help work on 'mkmatter' then please note that
  development is done by executing mkmatter through bundler, then
  mkmatter is released. If there are library problems when installing
  either way.. Then submit an issue <a href="https://github.com/IotaSpencer/mkmatter/issues">here</a>.

  Please include any tracebacks and the output of `mkmatter --debug`{: .highlight }
  </dd>
</dl>

## To Share or not To Share

{:.list-group .list-options .bg-dark}
<div class="d-flex">

{:.list-group-item .list-options-item .bg-dark .list-unstyled}
* ### User Install

  `$ gem install --user-install mkmatter`{: .highlight .d-block}

{:.list-group-item .list-options-item .bg-dark .list-unstyled}
* ### System-wide Install

  `$ sudo gem install mkmatter`{: .highlight .d-block}
  `$ gem install mkmatter`{: .highlight .d-block}
</div>

------

Doing such will install mkmatter and all its needed gems to whichever path is applicable for the width of its installation.
This most likely will include 'micro-install' a script that 'one-stop-shop' installs 'micro' a terminal text editor. 'micro' will be used by default if installed, unless `--editor=EDITORCOMMAND`{: .highlight } is provided.
</div>
