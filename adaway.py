#!/usr/bin/env python3
import requests

url_lists=['https://adaway.org/hosts.txt','https://goodbyeads.weebly.com/uploads/1/2/2/1/122145164/goodbyeads.txt','https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&showintro=0&mimetype=plaintext','https://someonewhocares.org/hosts/hosts']
file_lists = []
file_name = 'hosts'
text_search = '127.0.0.1'
text_replace = '0.0.0.0'
final_file = 'final_host.txt'

def get_files(url,file_name):
  print('Beginning file download with requests')
  r = requests.get(url, stream=True)
  with open(file_name, 'wb') as f:
    f.write(r.content)
  print(r.status_code)
  print(r.headers['content-type'])
  print(r.encoding)
  print(file_name)
  file_lists.append(file_name)
  print file_lists

def sort_files(file_name,text_search,text_replace):
  # Read in the file
  print('sorting file...')
  with open(file_name, 'r') as file :
    filedata = file.read()
    # Replace the target string
  filedata = filedata.replace(text_search,text_replace)
  # Write the file out again
  with open(file_name, 'w') as file:
    file.write(filedata)
    
    
def merge_files(output_file,file_list):
  with open(output_file, 'w') as outfile:
      for fname in file_list:
          with open(fname) as infile:
              for line in infile:
                  outfile.write(line)    

for i in url_lists:
  get_files(i,file_name+str(url_lists.index(i)))
  sort_files(file_name+str(url_lists.index(i)),text_search,text_replace)  
  
#print file_lists
merge_files(final_file,file_lists) 
with open(final_file, 'r') as file :
  filedata = file.read()
    # Replace the target string
  filedata = filedata.replace(text_replace,text_search,1)
  # Write the file out again
  with open(final_file, 'w') as file:
    file.write(filedata)
