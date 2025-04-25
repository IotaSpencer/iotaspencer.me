#! /home/ken/repos/is.me-redux/.venv/bin/python3
# import os
import subprocess
import paramiko 
from pysftp import Connection as pConnection
from fabric import Connection as fConnection
import increment_file
import os

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

def main():
  logger.info("Logging Started")
  logger.info("Starting build()")
  build_n_tar()
  logger.info("Build complete")
  logger.info("Starting push() & checking for uname and git")
  push()
  logger.info("Push complete")
  logger.info("Extraction started")
  extract()
  logger.info("Extraction complete")
  
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
def build_n_tar():
  install = subprocess.run(["bundle", "install"], check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  for line in install.stdout.decode().splitlines():
    logger.info("        %s", line)
  logger.info("'bundle install' complete")
  # logger.info(install.stdout)
  os.environ['JEKYLL_ENV'] = 'production'
  build = subprocess.run(["bundle", "exec", "jekyll", "build"], env= os.environ,  check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  for line in build.stdout.decode().splitlines():
    logger.info("        %s", line)
  logger.info("'bundle exec jekyll build' complete")
  logger.info("Starting tar")
  filename = increment_file.get_next_filename("_dist/site_{}.tar.gz")
  logger.info(f"        Creating {filename}")
  tar = subprocess.run(["tar", "-cvzf", filename, "_site"], check=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  for line in tar.stdout.decode().splitlines():
    logger.info("        %s", line)
  logger.info("tar complete")

  
if __name__ == '__main__':
  main()
  logger.info("Build&Push complete")