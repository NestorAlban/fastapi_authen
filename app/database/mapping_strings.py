

class Mapping_rath():
    def __init__(self) -> None:
        pass

    
    
    def role_mapping(role: int):
        print("=========role===============")
        roles = {
            0: "user",
            1: "worker level 1",
            2: "worker level 2"
        }
        role_name = None
        
        print(f'{role} got')
        if role in roles:
            print("exist")
            role_name = roles.get(role)
        else:
            print("existn")
        print("=========role===============")
        return role_name


    


