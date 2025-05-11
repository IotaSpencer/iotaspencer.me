---
layout: page
title: Usage
breadcrumb: Usage
categories:
- Jekyll
- mkmatter
- Usage
tags:
- mkmatter
- usage
permalink: /projects/mkmatter/guide/usage/index.html
date: '2018-03-04 06:52:40 -0500'
---
{::options parse_block_html="true" /}
<div class="float-right card bg-dark ml-4 mr-2" style="order: 2;">

# Contents
{:.no_toc .mx-auto}

* TOC
{:toc class="well bg-dark d-inline-block pr-3 py-2"}
</div>

<div>
<h1>{{ page.title }}</h1>

## Note Before Reading
Please read <a href="{% link projects/mkmatter/guide/installation.md %}">Installation</a> before reading this page.

At this point, if you haven't already, you should probably run 'micro-install'
if you want to use 'micro' the terminal text editor.
<hr class="d-flex">

## Commands

### New (mkmatter new)

##### Post (mkmatter new --type post)

<div class="list-group list-options bg-dark-gray d-flex">
<div class="list-group-item list-options-item bg-dark-gray">

<h6 class="no_toc bg-dark-gray list-group-header list-options-header d-inline-block p-2">Options</h6>

* `--publish`{:.highlight}
  * Whether to publish the following post.
  * This has no effect if not used with `--file`{:.highlight}
* `--dry-run`{:.highlight}
  * Save the answers to a file named in the format of `YEAR-MONTH-DAY-TITLE.format`{:.highlight}


</div></div>

##### Page (mkmatter new  --type page)

<div class="list-group list-options bg-dark-gray d-flex">
<div class="list-group-item list-options-item bg-dark-gray">

<h6 class="no_toc bg-dark-gray list-group-header list-options-header d-inline-block p-2">Options</h6>

* `--publish`{:.highlight}
* `--file`{:.highlight}

</div></div>

### Tags (mkmatter tags)

##### Find (mkmatter tags find)

##### Gen (mkmatter tags gen)

<div class="list-group list-options bg-dark-gray d-flex">
<div class="list-group-item list-options-item bg-dark-gray">

<h6 class="no_toc bg-dark-gray list-group-header d-inline-block p-2">Options</h6>

* `--tag-index=TAG-INDEX`{:.highlight}, `-i`{:.highlight}
  * Configures whether, while generating the tag files, if and what layout they will be given
  * If you don't have a tag index, omit `--tag-index`{:.highlight}
* `--dry-run`{:.highlight}

</div></div>

##### New (mkmatter tags new)
</div>
