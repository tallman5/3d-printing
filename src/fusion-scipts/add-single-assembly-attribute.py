# Author: tallman#9584 on Discord
# Description: This is a helper for the Export BOM script.
#   A component can be tagged as a "single assembly."
#   Which means, during the export, only one line item is added to the BOM.
#   The child assemblies and components are included in the image taken of the component.

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        product = app.activeProduct

        design = adsk.fusion.Design.cast(product)
        if not design:
            ui.messageBox('Please change to MODEL workspace and try again.')
            return

        activeComponent = design.activeComponent
        attributes = activeComponent.attributes

        attributeAdded = False
        for attribute in attributes:
            if attribute.groupName == 'exportBom':
                if attribute.name == 'isSingleAssembly':
                    attribute.value = 'True'
                    attributeAdded = True
        
        if attributeAdded == False:
            attributes.add('exportBom', 'isSingleAssembly', 'True')

        ui.messageBox('Done!')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
