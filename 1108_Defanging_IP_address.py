# with replace
def defangIPaddr(address):
  new_address = address.replace(".","[.]")
  return new_address
    
# without replace

def defangIPaddr(address):
  address = address.split(".")
  new_add= "[.]".join(address)
  return new_add
    
