from copier_templates_extensions import ContextHook    

class ContextUpdater(ContextHook):

    def hook(self, context: dict) -> dict:
        """Add hook to update context based on user's input."""
        if context["plugin_type"] == "Controller":
            context["module_import"] = "controller"
            context["plugin_base"] = "ComputationalController"
            context["class_baseline"] = "MyController"
        else:
            if context["plugin_engine"] == "ExEngine":
                context = self._chose_exengine_context(context)
            else: # Bluesky
                context = self._chose_bluesky_context(context)        
            context = self._set_config_info(context)
        context["plugin_engine"] = context["plugin_engine"].lower()
        return context
    
    ########################################################
    ################ ExEngine context ######################
    ########################################################
    def _chose_exengine_context(self, context: dict) -> dict:
        """Select which ExEngine model base class to use."""
        if context["plugin_type"] == "Model":
            context["module_import"] = "model"
            if context["plugin_model_type"] == "Detector":
                context = self._chose_exengine_detector(context)
            else: # motor model
                context = self._chose_exengine_motor(context)
        return context
    
    def _chose_exengine_detector(self, context: dict) -> dict:
        """Select which detector model base class to use."""
        if context["mm_support"]:
            context["plugin_base"] = "ExEngineMMCameraModel"
        else:
            context["plugin_base"] = "ExEngineDetectorModel"
        context["class_baseline"] = "MyDetectorModel"
        return context
    
    def _chose_exengine_motor(self, context: dict) -> dict:
        """Select which motor model base class to use."""
        if context["plugin_motor_type"] == "Single":
            if context["mm_support"]:
                context["plugin_base"] = "ExEngineMMSingleMotorModel"
            else:
                context["plugin_base"] = "ExEngineSingleMotorModel"
        else: # dual-axis (XY) motor
            if context["mm_support"]:
                context["plugin_base"] = "ExEngineMMDoubleMotorModel"
            else:
                context["plugin_base"] = "ExEngineDoubleMotorModel"
        context["class_baseline"] = "MyMotorModel"
        return context
    
    def _set_config_info(self, context: dict) -> dict:
        """Set config_info and config_base based on plugin_type."""
        if context["plugin_type"] == "Model":
            if context["plugin_model_type"] == "Detector":
                context["config_base"] = "DetectorModelInfo"
                context["config_info"] = "MyDetectorInfo"
            else: # motor model
                context["config_base"] = "MotorModelInfo"
                context["config_info"] = "MyMotorInfo"
        return context
    
    ########################################################
    ################# Bluesky context ######################
    ########################################################
    def _chose_bluesky_context(self, context: dict) -> dict:
        """Select which Bluesky model base class to use."""
        if context["plugin_type"] == "Model":
            context["module_import"] = "model"
            if context["plugin_model_type"] == "Detector":
                context = self._set_bluesky_detector(context)
            else: # motor model
                context = self._set_bluesky_motor(context)
        return context
    
    def _set_bluesky_detector(self, context: dict) -> dict:
        """Set Bluesky detector model base class."""
        context["plugin_base"] = "BlueskyDetectorModel"
        context["class_baseline"] = "MyDetectorModel"
        return context
    
    def _set_bluesky_motor(self, context: dict) -> dict:
        """Select which Bluesky motor model base class to use."""
        context["plugin_base"] = "BlueskyMotorModel"
        context["class_baseline"] = "MyMotorModel"
        return context
    
    