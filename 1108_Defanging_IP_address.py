# with replace
def defangIPaddr(self, address: str) -> str:
  new_address = address.replace(".","[.]")
  return new_address
    
# without replace

def defangIPaddr(self, address: str) -> str:
  address = address.split(".")
  new_add= "[.]".join(address)
  return new_add
    
