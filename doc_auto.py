#!/usr/bin/python3

import docker
import requests

def main():
  client = docker.from_env()
  image_list = client.images.list()

for image in image_list:
  print('We found a image! Name: ' + image.name)
img = input('select image')
 
client.images.pull(img)

 
  portstart = 10000
  count = input('number of containers to test')
   container = client.containers.create(img,ports={'80/tcp':portstart+a})
   container.start()
    print('Created container number {} name: {}'.format(a,container.name))

  container_list = client.containers.list()
  count = 0
    port = container.attrs['HostConfig']['PortBindings']['80/tcp'][0]['HostPort']
    r = requests.get('http://127.0.0.1:{}'.format(port))
    if(r.status_code == 200):
      print('Container {} is alive and working on port {}!'.format(container.name,port))
      count += 1
    else:
      print('Container {} is dead :( Code: {}'.format(container.name,r.status_code))

  print('Summary: Online Containers: {} Offline Containers: {}'.format(count,len(container_list)-count))
  print('Removing containers...')
 
    container.stop()
    container.remove()

if __name__ == "__main__":
    main()
