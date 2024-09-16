# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .step_destination import StepDestination
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.pydantic_utilities import update_forward_refs


class HandoffStep(UniversalBaseModel):
    block: typing.Optional["HandoffStepBlock"] = pydantic.Field(default=None)
    """
    This is the block to use. To use an existing block, use `blockId`.
    """

    destinations: typing.Optional[typing.List[StepDestination]] = pydantic.Field(default=None)
    """
    These are the destinations that the step can go to after it's done.
    """

    name: str = pydantic.Field()
    """
    This is the name of the step.
    """

    block_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="blockId")] = pydantic.Field(
        default=None
    )
    """
    This is the id of the block to use. To use a transient block, use `block`.
    """

    input: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    This is the input to the block. You can use any key-value map as input to the block.
    
    Example:
    {
    "name": "John Doe",
    "age": 20
    }
    
    You can reference any variable in the context of the current block:
    
    - "{{your-step-name.output.your-property-name}}" for another step's output (in the same workflow; read caveat #1)
    - "{{your-step-name.input.your-property-name}}" for another step's input (in the same workflow; read caveat #1)
    - "{{your-block-name.output.your-property-name}}" for another block's output (in the same workflow; read caveat #2)
    - "{{your-block-name.input.your-property-name}}" for another block's input (in the same workflow; read caveat #2)
    - "{{workflow.input.your-property-name}}" for the current workflow's input
    - "{{global.your-property-name}}" for the global context
    
    Example:
    {
    "name": "{{my-tool-call-step.output.name}}",
    "age": "{{my-tool-call-step.input.age}}",
    "date": "{{workflow.input.date}}"
    }
    
    You can dynamically change the key name.
    
    Example:
    {
    "{{my-tool-call-step.output.key-name-for-name}}": "{{name}}",
    "{{my-tool-call-step.input.key-name-for-age}}": "{{age}}",
    "{{workflow.input.key-name-for-date}}": "{{date}}"
    }
    
    You can represent the value as a string, number, boolean, array, or object.
    
    Example:
    {
    "name": "john",
    "age": 20,
    "date": "2021-01-01",
    "metadata": {
    "unique-key": "{{my-tool-call-step.output.unique-key}}"
    },
    "array": ["A", "B", "C"],
    }
    
    Caveats:
    
    1. a workflow can execute a step multiple times. example, if a loop is used in the graph. {{stepName.input/output.propertyName}} will reference the latest usage of the step.
    2. a workflow can execute a block multiple times. example, if a step is called multiple times or if a block is used in multiple steps. {{blockName.input/output.propertyName}} will reference the latest usage of the block. this liquid variable is just provided for convenience when creating blocks outside of a workflow.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .callback_step import CallbackStep  # noqa: E402
from .create_workflow_block_dto import CreateWorkflowBlockDto  # noqa: E402
from .handoff_step_block import HandoffStepBlock  # noqa: E402

update_forward_refs(CallbackStep, HandoffStep=HandoffStep)
update_forward_refs(CreateWorkflowBlockDto, HandoffStep=HandoffStep)
update_forward_refs(HandoffStep)
