import os


try:
    PROJECT_ROOT_PATH = os.path.abspath(os.path.join(__file__, '../..'))
except NameError:
    PROJECT_ROOT_PATH = os.path.abspath(os.path.join(os.getcwd()))
    
    
class DataPaths:
    def __init__(self, base_path='/net/nfs.corp/s2-research/recommender/scidocs_v1'):
        self.base_path = base_path
        
        self.cite_val = os.path.join(base_path, 'cite', 'val.qrel')
        self.cite_test = os.path.join(base_path, 'cite', 'test.qrel')
        
        self.cocite_val = os.path.join(base_path, 'cocite', 'val.qrel')
        self.cocite_test = os.path.join(base_path, 'cocite', 'test.qrel')

        self.coread_val = os.path.join(base_path, 'coread', 'val.qrel')
        self.coread_test = os.path.join(base_path, 'coread', 'test.qrel')
        
        self.coview_val = os.path.join(base_path, 'coview', 'val.qrel')
        self.coview_test = os.path.join(base_path, 'coview', 'test.qrel')
        
        self.mag_train = os.path.join(base_path, 'mag', 'train.csv')
        self.mag_val = os.path.join(base_path, 'mag', 'val.csv')
        self.mag_test = os.path.join(base_path, 'mag', 'test.csv')
        
        self.mesh_train = os.path.join(base_path, 'mesh', 'train.csv')
        self.mesh_val = os.path.join(base_path, 'mesh', 'val.csv')
        self.mesh_test = os.path.join(base_path, 'mesh', 'test.csv')
        
        self.recomm_train = os.path.join(base_path, 'recomm', 'train.csv')
        self.recomm_val = os.path.join(base_path, 'recomm', 'val.csv')
        self.recomm_test = os.path.join(base_path, 'recomm', 'test.csv')
        self.recomm_propensity_scores = os.path.join(base_path, 'recomm', 'propensity_scores.json')
        
        self.paper_metadata = os.path.join(base_path, 'paper_metadata.json')