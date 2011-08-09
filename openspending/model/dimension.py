from . import base

collection = 'dimension'

base.init_model_module(__name__, collection)

# dimension objects probably have the following fields
#   _id
#   label
#   coll - Collection
#   context
#   key

def create(dataset_name, key, label, description=None, **kwargs):
    kwargs.update({"dataset": dataset_name,
                   "key": key,
                   "label": label,
                   "description": description})
    return base.update(collection,
                       {"dataset": dataset_name, "key": key},
                       kwargs,
                       upsert=True,
                       manipulate=True)

def get_dataset_dimensions(dataset_name, facets_only=False):
    query = {"dataset": dataset_name}
    if facets_only:
        query['facet'] = True
    return base.find(collection, query)

