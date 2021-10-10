# coding=utf-8
""" Base Pre-Processor token used in other classes to represent directives """
from __future__ import annotations

from os import PathLike
from antlr4 import ParserRuleContext
from abc import ABC, abstractmethod
from typing import Union, Optional, Any, List, TYPE_CHECKING

from ...abc import ParacLogicToken, NULL_CHILDREN

if TYPE_CHECKING:
    from ..ctx import FilePreProcessorContext

__all__ = [
    'PreProcessorLogicToken'
]


class PreProcessorLogicToken(ParacLogicToken, ABC):
    """ Pre-Processor Logic-Token, which is used to represent Directives """

    @abstractmethod
    def __init__(
            self,
            name: str,
            as_str: str,
            line: int,
            column: int,
            parent_file: FilePreProcessorContext,
            relative_parent_file_name: Union[str, PathLike],
            antlr4_ctx: ParserRuleContext,
            parent: Optional[Any] = None,
            children: Optional[List[Any]] = NULL_CHILDREN,
    ):
        self._parent_file = parent_file
        super().__init__(
            name, as_str, line, column, relative_parent_file_name,
            antlr4_ctx, parent, children
        )

    def get_as_str(self) -> str:
        """ Gets the value of the Pre-Processor token as a string """
        return self.extract_original_text()

    @property
    @abstractmethod
    def parent_file(self) -> FilePreProcessorContext:
        """ Returns the parent file context instance """
        return self._parent_file

    @abstractmethod
    def is_directive(self) -> bool:
        """ Returns whether the token is a directive """
        ...

    @abstractmethod
    def has_children(self) -> bool:
        """ Returns whether the token has children that are other tokens """
        ...

    @abstractmethod
    def has_code_block_scope(self) -> bool:
        """
        Returns whether it is possible to pass a code-block after the
        item. If this is False, then has_code_block_child can only be
        False as well
        """
        ...

    @abstractmethod
    def has_code_block_child(self) -> bool:
        """
        Returns whether the token has code-block children that are associated
        with the tokens scope
        """
        ...
