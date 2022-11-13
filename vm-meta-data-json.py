import httplib2
import json

http = httplib2.Http()

def query_metadata(key):
 # the metadata is stored in json format using the  vaule  ?recursive=true to the Metadata of the instance
 response , content = http.request('http://metadata.google.internal/computeMetadata/v1/instance/?recursive=true',
                                   headers={'Metadata-Flavor': 'True'})
 if response != 500:
            #print(content)
  d = json.loads(content)
  #print(type(d))

 for i in d:
    if i == key:
     print(d[key])
    #print(i)
if __name__ == '__main__':
 data_key = input("enter the key (attributes/disks/hostname/id/image/machine-type/network-interfaces/scheduling/maintenance-event/project-id/service-accounts/tags/zone):\n ")
 query_metadata(data_key)
