---
layout: post
title: Jekyllposter Tutorial
categories:
- Tutorial
- Jekyll
- Ruby-Gems
tags:
- tutorial
- jekyllposter
date: '2018-01-29 14:38:29 -0500'
published: true
draft: false
toc: true
share: true
gem: jekyllposter
---
# {{ page.gem | capitalize }} - A Tutorial

## Installation

### Root or System Wide Installation

{% highlight ruby %}
gem install {{ page.gem }}
{% endhighlight %}

### Non-Root

Sometimes you want to use gems in a project of your own, that's where non-root installs are handy.

#### Project Install

If you haven't already, put
`gem '{{ page.gem }}'` on a line in your Gemfile or as a `.add_runtime_dependency` and then run `bundle install`

#### Account Install

`gem install --user-install {{ page.gem }}`

## Usage

First off, when you want to use mkmatter, make sure you are directly above your jekyll site root. This is also what this tutorial assumes.
**ProTip**: *if you have to use* `'..'` *then you are not above the directory.*
