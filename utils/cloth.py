class Cloth:
    def __init__(self, id, path, description):
        self.id = id
        self.path = path
        self.description = description
    def __repr__(self):
        return f"Cloth(id={self.id}, path={self.path}, description={self.description})"
    
    def get_cloth_description(self):
        return self.description
    
    def get_cloth_path(self):
        return self.path
    
    def get_cloth_id(self):
        return self.id
        