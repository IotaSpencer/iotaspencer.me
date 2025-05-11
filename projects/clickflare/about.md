## clickflare - Interface with the Cloudflare API!

    clickflare is an interface into the Cloudflare API,
    usage is rate-limited by Cloudflare itself, not the gem.

    See https://api.cloudflare.com/#getting-started-requests for information
    on the API and the linked anchor for rate-limiting specifically.

v0.0.3-alpha.3

### Global Options

### --api-key APIKEY

Cloudflare API Key

Default Value
: none


### --email EMAIL

Cloudflare E-Mail

Default Value
: none


### --help
Show this message


### --version
Display the program version


### Commands

#### Command: `dns-record `

DNS Record Management

##### Commands

###### Command: `add `

add a record

###### Command: `rem|del|delete `

remove a record

###### Command: `show `

get a record

###### Command: `update|modify `

update a record

#### Command: `help  command`

Shows a list of commands or help for one command

Gets help for the application or its commands. Can also list the commands in a
way helpful to creating a bash-style completion function

##### Options

##### -c
List commands one per line, to assist with shell completion


#### Command: `initconfig `
Initialize the config file using current global options

Initializes a configuration file where you can set default options for command
line flags, both globally and on a per-command basis.  These defaults override
the built-in defaults and allow you to omit commonly-used command line flags
when invoking this program

##### Options

##### --[no-]force
force overwrite of existing config file


#### Command: `ips `
Return Cloudflare IPs

##### Commands

###### Command: `list `
list out cloudflare's IPs

Default Command
:   list

#### Command: `zones `
Use all the non-dns '/zones/*' endpoints

##### Commands

###### Command: `all|list `
list all zones or filter them

Default Command
:   all

