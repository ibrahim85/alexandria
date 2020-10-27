from alexandria.dataset import DatasetManager
from alexandria.models import ModelsManager

class Experiment:
    def __init__(self, name, dataset=None, xlabels=None, ylabels=None, libs=None, models=None, modellibdict=None):
        if type(name) == str:
            self.name = name
        else:
            raise ValueError('Experiment \'name\' argument must be string, not {}'.format(  str( type( name ) ) ))
        
        # Initialize the dataset manager object
        self.dm = DatasetManager()
        if type(dataset) != type(None):
            if type(xlabels) == type(None) or type(ylabels) == type(None):
                self.dm.setData(dataset)
            else:
                self.dm.setData(dataset=dataset, xlabels=xlabels, ylabels=ylabels)

        # Initialize the models object
        self.mm = ModelsManager()

        # Add the provided model information
        self.addModels(libs=libs, models=models, modellibdict=modellibdict)

    # This method only exists to allow for users to feel more comfortable with the API  
    def addModel(self, lib=None, model=None, modellibdict=None):
        self.addModels(libs=lib, models=model, modellibdict=modellibdict)

    def addModels(self, modellibdict=None, libs=None, models=None):
        # We can hand this data over
        if modellibdict != None:
            self.mm.addModels( modellibdict )

        # If model values were specified, we must translate them into a dictionary
        #   for the model manager
        else:
            if libs != None and models != None:
                modellibdict = self.createForModelsManager(libs=libs, models=models)
                self.mm.addModels( modellibdict )


    def createForModelsManager(self, libs=[], models=[]):
        return_dict = dict()

        # If the libs argument is a string, then add all the models with this library
        if type(libs) == str:
            lib = libs
            return_dict[ lib ] = models
        elif type(libs) == list:
            if type(models) == list:
                if len(models) == len(libs):
                    for lib, model in zip(libs, models):
                        if lib in return_dict:
                            return_dict[ lib ].append(model)
                        else:
                            return_dict[ lib ] = [ model ]


        return return_dict                            

        

    def getName(self):
        return self.name
    def setName(self, name):
        if type(name) == str:
            self.name = name
        else:
            raise ValueError('Experiment \'name\' argument must be string, not {}'.format(  str( type( name ) ) ))
       
    def getModels(self, aslist=False):
        return self.mm.getModels(aslist)

    def getNumModels(self):
        return len(self.mm.getNumModels())