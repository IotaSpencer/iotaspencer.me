#! /home/ken/repos/iotaspencer.me/.venv/bin/python3 -B

# import os
import subprocess
import paramiko 
from pysftp import Connection as pConnection
from fabric import Connection as fConnection
import increment_file
import os
from pathlib import Path
import click
import logging

def remove_non_needed(record):
  if record.name == "paramiko.transport" and record.levelname == 'DEBUG':
    return False
  if record.name == "invoke" and record.levelname == 'DEBUG':
    return False
  if record.name == "b&p" and record.msg.startswith('        Using '):
    return False
  return True

logging.getLogger("paramiko.transport").addFilter(remove_non_needed)
logging.getLogger("invoke").addFilter(remove_non_needed)
handler = logging.StreamHandler()
bf = logging.Formatter('    {asctime} {name} {levelname:8s} {message}',
                       style='{')
logger = logging.getLogger("b&p")
logger.addFilter(remove_non_needed)
logging.basicConfig(level=logging.DEBUG, handlers=[handler], format='{asctime} {name} {levelname:8s} {message}', style='{', datefmt='%Y-%m-%d %H:%M:%S')

def extract():
  # logger.info("Checking if tar runs")
  # tar = fConnection(host='spidey', user='root', connect_kwargs={
  #               "key_filename": "/home/ken/.ssh/id_rsa",
  #           }).run('tar --version')
  # logger.info('tar check complete')

  logger.info('Extracting tar file on remote server')
  extract_tar = fConnection(host='spidey', user='root', connect_kwargs={
                "key_filename": "/home/ken/.ssh/id_rsa",
            }).run('cd /var/www && tar --strip-components=1 -vxzf site.tar.gz -C /var/www/iotaspencer-me')
  logger.info('Remote extraction complete')
  
def push():
  # logger.info('Checking if uname runs')
  # uname = fConnection(host='spidey', user='root', connect_kwargs={
  #               "key_filename": "/home/ken/.ssh/id_rsa",
  #           }).run('uname -s')
  # # logger.info(str(uname))
  # logger.info('uname complete')
  # logger.info('Checking if git runs')
  # git = fConnection(host='spidey', user='root', connect_kwargs={
  #               "key_filename": "/home/ken/.ssh/id_rsa",
  #           }).run('git --version')
  # logger.info(str(git))
  # ssh = paramiko.SSHClient()
  tar_put = fConnection(host='spidey', user='root', connect_kwargs={
                "key_filename": "/home/ken/.ssh/id_rsa",
            }).put(increment_file.get_latest_filename("_dist/site_{}.tar.gz"), "/var/www/site.tar.gz")
  
  logger.info('tar put complete')
  logger.info('Checking if ls contains tar file')
  ls_run = fConnection(host='spidey', user='root', connect_kwargs={
                "key_filename": "/home/ken/.ssh/id_rsa",
            }).run('ls -l /var/www')
  logger.info('ls complete')
  
  
def build_n_tar(build_args):
  build_command = ["bundle", "exec", "jekyll", "build"]
  if len(build_args) > 0:
    build_command.extend(build_args)
  logger.info("Starting 'bundle install'")
  install = subprocess.run(["bundle", "install"], check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  for line in install.stdout.decode().splitlines():
    logger.info("        %s", line)
  logger.info("'bundle install' complete")
  # logger.info(install.stdout)
  logger.info(f"Starting '{build_command}'")
  os.environ['JEKYLL_ENV'] = 'production'
  build = subprocess.run(build_command, env=os.environ,  check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  for line in build.stdout.decode().splitlines():
    logger.info("        %s", line)
  logger.info(f"'{build_command}' complete")
  logger.info("Starting tar")
  filename = increment_file.get_next_filename("_dist/site_{}.tar.gz")
  logger.info(f"        Creating {filename}")
  tar = subprocess.run(["tar", "-cvzf", filename, "_site"], check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  for line in tar.stdout.decode().splitlines():
    logger.info("        %s", line)
  logger.info("tar complete")

@click.group()
def cli():
  """
  Group for build and push commands.
  """
  pass
@cli.command(context_settings=dict(ignore_unknown_options=True, allow_extra_args=True, allow_interspersed_args=False))
@click.argument('build_args', nargs=-1, type=click.UNPROCESSED)
def btp(build_args):
  """
  Build, tar, and push the site to the remote server.
  """
  logger.info("Starting btp()")
  build_n_tar(build_args)
  logger.info("Build complete")
  push()
  logger.info("Push complete")
  extract()

@cli.command()
def clear():
  """
  Clear the _dist directory.
  """
  logger.info("Starting clear()")
  dist = Path("_dist")
  for child in dist.iterdir():
    if child.is_file() and child.name.startswith("site_") and child.name.endswith(".tar.gz"):
      logger.info(f"        Removing {child}")
      child.unlink() 
  glob = "_dist/site_*.tar.gz"
  logger.info(f"        Removing {dist}")
  
  logger.info("clear_dist complete")
if __name__ == '__main__':
  cli()
  logger.info("Build&Push complete")