# Generated from Anatomy.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .AnatomyParser import AnatomyParser
else:
    from AnatomyParser import AnatomyParser

# This class defines a complete listener for a parse tree produced by AnatomyParser.
class AnatomyListener(ParseTreeListener):

    # Enter a parse tree produced by AnatomyParser#program.
    def enterProgram(self, ctx:AnatomyParser.ProgramContext):
        pass

    # Exit a parse tree produced by AnatomyParser#program.
    def exitProgram(self, ctx:AnatomyParser.ProgramContext):
        pass


    # Enter a parse tree produced by AnatomyParser#expression.
    def enterExpression(self, ctx:AnatomyParser.ExpressionContext):
        pass

    # Exit a parse tree produced by AnatomyParser#expression.
    def exitExpression(self, ctx:AnatomyParser.ExpressionContext):
        pass


    # Enter a parse tree produced by AnatomyParser#statement.
    def enterStatement(self, ctx:AnatomyParser.StatementContext):
        pass

    # Exit a parse tree produced by AnatomyParser#statement.
    def exitStatement(self, ctx:AnatomyParser.StatementContext):
        pass


    # Enter a parse tree produced by AnatomyParser#show.
    def enterShow(self, ctx:AnatomyParser.ShowContext):
        pass

    # Exit a parse tree produced by AnatomyParser#show.
    def exitShow(self, ctx:AnatomyParser.ShowContext):
        pass


    # Enter a parse tree produced by AnatomyParser#control.
    def enterControl(self, ctx:AnatomyParser.ControlContext):
        pass

    # Exit a parse tree produced by AnatomyParser#control.
    def exitControl(self, ctx:AnatomyParser.ControlContext):
        pass


    # Enter a parse tree produced by AnatomyParser#function.
    def enterFunction(self, ctx:AnatomyParser.FunctionContext):
        pass

    # Exit a parse tree produced by AnatomyParser#function.
    def exitFunction(self, ctx:AnatomyParser.FunctionContext):
        pass


    # Enter a parse tree produced by AnatomyParser#fileOp.
    def enterFileOp(self, ctx:AnatomyParser.FileOpContext):
        pass

    # Exit a parse tree produced by AnatomyParser#fileOp.
    def exitFileOp(self, ctx:AnatomyParser.FileOpContext):
        pass


    # Enter a parse tree produced by AnatomyParser#blank.
    def enterBlank(self, ctx:AnatomyParser.BlankContext):
        pass

    # Exit a parse tree produced by AnatomyParser#blank.
    def exitBlank(self, ctx:AnatomyParser.BlankContext):
        pass


    # Enter a parse tree produced by AnatomyParser#assign.
    def enterAssign(self, ctx:AnatomyParser.AssignContext):
        pass

    # Exit a parse tree produced by AnatomyParser#assign.
    def exitAssign(self, ctx:AnatomyParser.AssignContext):
        pass


    # Enter a parse tree produced by AnatomyParser#functionStatement.
    def enterFunctionStatement(self, ctx:AnatomyParser.FunctionStatementContext):
        pass

    # Exit a parse tree produced by AnatomyParser#functionStatement.
    def exitFunctionStatement(self, ctx:AnatomyParser.FunctionStatementContext):
        pass


    # Enter a parse tree produced by AnatomyParser#parametros.
    def enterParametros(self, ctx:AnatomyParser.ParametrosContext):
        pass

    # Exit a parse tree produced by AnatomyParser#parametros.
    def exitParametros(self, ctx:AnatomyParser.ParametrosContext):
        pass


    # Enter a parse tree produced by AnatomyParser#args.
    def enterArgs(self, ctx:AnatomyParser.ArgsContext):
        pass

    # Exit a parse tree produced by AnatomyParser#args.
    def exitArgs(self, ctx:AnatomyParser.ArgsContext):
        pass


    # Enter a parse tree produced by AnatomyParser#structureControl.
    def enterStructureControl(self, ctx:AnatomyParser.StructureControlContext):
        pass

    # Exit a parse tree produced by AnatomyParser#structureControl.
    def exitStructureControl(self, ctx:AnatomyParser.StructureControlContext):
        pass


    # Enter a parse tree produced by AnatomyParser#if.
    def enterIf(self, ctx:AnatomyParser.IfContext):
        pass

    # Exit a parse tree produced by AnatomyParser#if.
    def exitIf(self, ctx:AnatomyParser.IfContext):
        pass


    # Enter a parse tree produced by AnatomyParser#ifElse.
    def enterIfElse(self, ctx:AnatomyParser.IfElseContext):
        pass

    # Exit a parse tree produced by AnatomyParser#ifElse.
    def exitIfElse(self, ctx:AnatomyParser.IfElseContext):
        pass


    # Enter a parse tree produced by AnatomyParser#while.
    def enterWhile(self, ctx:AnatomyParser.WhileContext):
        pass

    # Exit a parse tree produced by AnatomyParser#while.
    def exitWhile(self, ctx:AnatomyParser.WhileContext):
        pass


    # Enter a parse tree produced by AnatomyParser#for.
    def enterFor(self, ctx:AnatomyParser.ForContext):
        pass

    # Exit a parse tree produced by AnatomyParser#for.
    def exitFor(self, ctx:AnatomyParser.ForContext):
        pass


    # Enter a parse tree produced by AnatomyParser#read.
    def enterRead(self, ctx:AnatomyParser.ReadContext):
        pass

    # Exit a parse tree produced by AnatomyParser#read.
    def exitRead(self, ctx:AnatomyParser.ReadContext):
        pass


    # Enter a parse tree produced by AnatomyParser#printExpr.
    def enterPrintExpr(self, ctx:AnatomyParser.PrintExprContext):
        pass

    # Exit a parse tree produced by AnatomyParser#printExpr.
    def exitPrintExpr(self, ctx:AnatomyParser.PrintExprContext):
        pass


    # Enter a parse tree produced by AnatomyParser#graph.
    def enterGraph(self, ctx:AnatomyParser.GraphContext):
        pass

    # Exit a parse tree produced by AnatomyParser#graph.
    def exitGraph(self, ctx:AnatomyParser.GraphContext):
        pass


    # Enter a parse tree produced by AnatomyParser#graphType.
    def enterGraphType(self, ctx:AnatomyParser.GraphTypeContext):
        pass

    # Exit a parse tree produced by AnatomyParser#graphType.
    def exitGraphType(self, ctx:AnatomyParser.GraphTypeContext):
        pass


    # Enter a parse tree produced by AnatomyParser#graphParams.
    def enterGraphParams(self, ctx:AnatomyParser.GraphParamsContext):
        pass

    # Exit a parse tree produced by AnatomyParser#graphParams.
    def exitGraphParams(self, ctx:AnatomyParser.GraphParamsContext):
        pass


    # Enter a parse tree produced by AnatomyParser#openFile.
    def enterOpenFile(self, ctx:AnatomyParser.OpenFileContext):
        pass

    # Exit a parse tree produced by AnatomyParser#openFile.
    def exitOpenFile(self, ctx:AnatomyParser.OpenFileContext):
        pass


    # Enter a parse tree produced by AnatomyParser#closeFile.
    def enterCloseFile(self, ctx:AnatomyParser.CloseFileContext):
        pass

    # Exit a parse tree produced by AnatomyParser#closeFile.
    def exitCloseFile(self, ctx:AnatomyParser.CloseFileContext):
        pass


    # Enter a parse tree produced by AnatomyParser#writeFile.
    def enterWriteFile(self, ctx:AnatomyParser.WriteFileContext):
        pass

    # Exit a parse tree produced by AnatomyParser#writeFile.
    def exitWriteFile(self, ctx:AnatomyParser.WriteFileContext):
        pass


    # Enter a parse tree produced by AnatomyParser#deleteFile.
    def enterDeleteFile(self, ctx:AnatomyParser.DeleteFileContext):
        pass

    # Exit a parse tree produced by AnatomyParser#deleteFile.
    def exitDeleteFile(self, ctx:AnatomyParser.DeleteFileContext):
        pass


    # Enter a parse tree produced by AnatomyParser#readingFile.
    def enterReadingFile(self, ctx:AnatomyParser.ReadingFileContext):
        pass

    # Exit a parse tree produced by AnatomyParser#readingFile.
    def exitReadingFile(self, ctx:AnatomyParser.ReadingFileContext):
        pass


    # Enter a parse tree produced by AnatomyParser#readLine.
    def enterReadLine(self, ctx:AnatomyParser.ReadLineContext):
        pass

    # Exit a parse tree produced by AnatomyParser#readLine.
    def exitReadLine(self, ctx:AnatomyParser.ReadLineContext):
        pass


    # Enter a parse tree produced by AnatomyParser#readAll.
    def enterReadAll(self, ctx:AnatomyParser.ReadAllContext):
        pass

    # Exit a parse tree produced by AnatomyParser#readAll.
    def exitReadAll(self, ctx:AnatomyParser.ReadAllContext):
        pass


    # Enter a parse tree produced by AnatomyParser#Logic.
    def enterLogic(self, ctx:AnatomyParser.LogicContext):
        pass

    # Exit a parse tree produced by AnatomyParser#Logic.
    def exitLogic(self, ctx:AnatomyParser.LogicContext):
        pass


    # Enter a parse tree produced by AnatomyParser#Aritmetic.
    def enterAritmetic(self, ctx:AnatomyParser.AritmeticContext):
        pass

    # Exit a parse tree produced by AnatomyParser#Aritmetic.
    def exitAritmetic(self, ctx:AnatomyParser.AritmeticContext):
        pass


    # Enter a parse tree produced by AnatomyParser#return.
    def enterReturn(self, ctx:AnatomyParser.ReturnContext):
        pass

    # Exit a parse tree produced by AnatomyParser#return.
    def exitReturn(self, ctx:AnatomyParser.ReturnContext):
        pass


    # Enter a parse tree produced by AnatomyParser#idL.
    def enterIdL(self, ctx:AnatomyParser.IdLContext):
        pass

    # Exit a parse tree produced by AnatomyParser#idL.
    def exitIdL(self, ctx:AnatomyParser.IdLContext):
        pass


    # Enter a parse tree produced by AnatomyParser#andOr.
    def enterAndOr(self, ctx:AnatomyParser.AndOrContext):
        pass

    # Exit a parse tree produced by AnatomyParser#andOr.
    def exitAndOr(self, ctx:AnatomyParser.AndOrContext):
        pass


    # Enter a parse tree produced by AnatomyParser#negation.
    def enterNegation(self, ctx:AnatomyParser.NegationContext):
        pass

    # Exit a parse tree produced by AnatomyParser#negation.
    def exitNegation(self, ctx:AnatomyParser.NegationContext):
        pass


    # Enter a parse tree produced by AnatomyParser#minor.
    def enterMinor(self, ctx:AnatomyParser.MinorContext):
        pass

    # Exit a parse tree produced by AnatomyParser#minor.
    def exitMinor(self, ctx:AnatomyParser.MinorContext):
        pass


    # Enter a parse tree produced by AnatomyParser#bool.
    def enterBool(self, ctx:AnatomyParser.BoolContext):
        pass

    # Exit a parse tree produced by AnatomyParser#bool.
    def exitBool(self, ctx:AnatomyParser.BoolContext):
        pass


    # Enter a parse tree produced by AnatomyParser#parensL.
    def enterParensL(self, ctx:AnatomyParser.ParensLContext):
        pass

    # Exit a parse tree produced by AnatomyParser#parensL.
    def exitParensL(self, ctx:AnatomyParser.ParensLContext):
        pass


    # Enter a parse tree produced by AnatomyParser#equals.
    def enterEquals(self, ctx:AnatomyParser.EqualsContext):
        pass

    # Exit a parse tree produced by AnatomyParser#equals.
    def exitEquals(self, ctx:AnatomyParser.EqualsContext):
        pass


    # Enter a parse tree produced by AnatomyParser#equalsL.
    def enterEqualsL(self, ctx:AnatomyParser.EqualsLContext):
        pass

    # Exit a parse tree produced by AnatomyParser#equalsL.
    def exitEqualsL(self, ctx:AnatomyParser.EqualsLContext):
        pass


    # Enter a parse tree produced by AnatomyParser#greater.
    def enterGreater(self, ctx:AnatomyParser.GreaterContext):
        pass

    # Exit a parse tree produced by AnatomyParser#greater.
    def exitGreater(self, ctx:AnatomyParser.GreaterContext):
        pass


    # Enter a parse tree produced by AnatomyParser#parens.
    def enterParens(self, ctx:AnatomyParser.ParensContext):
        pass

    # Exit a parse tree produced by AnatomyParser#parens.
    def exitParens(self, ctx:AnatomyParser.ParensContext):
        pass


    # Enter a parse tree produced by AnatomyParser#arrayAssign.
    def enterArrayAssign(self, ctx:AnatomyParser.ArrayAssignContext):
        pass

    # Exit a parse tree produced by AnatomyParser#arrayAssign.
    def exitArrayAssign(self, ctx:AnatomyParser.ArrayAssignContext):
        pass


    # Enter a parse tree produced by AnatomyParser#dot.
    def enterDot(self, ctx:AnatomyParser.DotContext):
        pass

    # Exit a parse tree produced by AnatomyParser#dot.
    def exitDot(self, ctx:AnatomyParser.DotContext):
        pass


    # Enter a parse tree produced by AnatomyParser#float.
    def enterFloat(self, ctx:AnatomyParser.FloatContext):
        pass

    # Exit a parse tree produced by AnatomyParser#float.
    def exitFloat(self, ctx:AnatomyParser.FloatContext):
        pass


    # Enter a parse tree produced by AnatomyParser#mulDiv.
    def enterMulDiv(self, ctx:AnatomyParser.MulDivContext):
        pass

    # Exit a parse tree produced by AnatomyParser#mulDiv.
    def exitMulDiv(self, ctx:AnatomyParser.MulDivContext):
        pass


    # Enter a parse tree produced by AnatomyParser#listAssign.
    def enterListAssign(self, ctx:AnatomyParser.ListAssignContext):
        pass

    # Exit a parse tree produced by AnatomyParser#listAssign.
    def exitListAssign(self, ctx:AnatomyParser.ListAssignContext):
        pass


    # Enter a parse tree produced by AnatomyParser#negative.
    def enterNegative(self, ctx:AnatomyParser.NegativeContext):
        pass

    # Exit a parse tree produced by AnatomyParser#negative.
    def exitNegative(self, ctx:AnatomyParser.NegativeContext):
        pass


    # Enter a parse tree produced by AnatomyParser#split.
    def enterSplit(self, ctx:AnatomyParser.SplitContext):
        pass

    # Exit a parse tree produced by AnatomyParser#split.
    def exitSplit(self, ctx:AnatomyParser.SplitContext):
        pass


    # Enter a parse tree produced by AnatomyParser#root.
    def enterRoot(self, ctx:AnatomyParser.RootContext):
        pass

    # Exit a parse tree produced by AnatomyParser#root.
    def exitRoot(self, ctx:AnatomyParser.RootContext):
        pass


    # Enter a parse tree produced by AnatomyParser#hex.
    def enterHex(self, ctx:AnatomyParser.HexContext):
        pass

    # Exit a parse tree produced by AnatomyParser#hex.
    def exitHex(self, ctx:AnatomyParser.HexContext):
        pass


    # Enter a parse tree produced by AnatomyParser#id.
    def enterId(self, ctx:AnatomyParser.IdContext):
        pass

    # Exit a parse tree produced by AnatomyParser#id.
    def exitId(self, ctx:AnatomyParser.IdContext):
        pass


    # Enter a parse tree produced by AnatomyParser#dictAssign.
    def enterDictAssign(self, ctx:AnatomyParser.DictAssignContext):
        pass

    # Exit a parse tree produced by AnatomyParser#dictAssign.
    def exitDictAssign(self, ctx:AnatomyParser.DictAssignContext):
        pass


    # Enter a parse tree produced by AnatomyParser#power.
    def enterPower(self, ctx:AnatomyParser.PowerContext):
        pass

    # Exit a parse tree produced by AnatomyParser#power.
    def exitPower(self, ctx:AnatomyParser.PowerContext):
        pass


    # Enter a parse tree produced by AnatomyParser#comp.
    def enterComp(self, ctx:AnatomyParser.CompContext):
        pass

    # Exit a parse tree produced by AnatomyParser#comp.
    def exitComp(self, ctx:AnatomyParser.CompContext):
        pass


    # Enter a parse tree produced by AnatomyParser#modDivent.
    def enterModDivent(self, ctx:AnatomyParser.ModDiventContext):
        pass

    # Exit a parse tree produced by AnatomyParser#modDivent.
    def exitModDivent(self, ctx:AnatomyParser.ModDiventContext):
        pass


    # Enter a parse tree produced by AnatomyParser#cross.
    def enterCross(self, ctx:AnatomyParser.CrossContext):
        pass

    # Exit a parse tree produced by AnatomyParser#cross.
    def exitCross(self, ctx:AnatomyParser.CrossContext):
        pass


    # Enter a parse tree produced by AnatomyParser#castInt.
    def enterCastInt(self, ctx:AnatomyParser.CastIntContext):
        pass

    # Exit a parse tree produced by AnatomyParser#castInt.
    def exitCastInt(self, ctx:AnatomyParser.CastIntContext):
        pass


    # Enter a parse tree produced by AnatomyParser#addSub.
    def enterAddSub(self, ctx:AnatomyParser.AddSubContext):
        pass

    # Exit a parse tree produced by AnatomyParser#addSub.
    def exitAddSub(self, ctx:AnatomyParser.AddSubContext):
        pass


    # Enter a parse tree produced by AnatomyParser#reverse.
    def enterReverse(self, ctx:AnatomyParser.ReverseContext):
        pass

    # Exit a parse tree produced by AnatomyParser#reverse.
    def exitReverse(self, ctx:AnatomyParser.ReverseContext):
        pass


    # Enter a parse tree produced by AnatomyParser#int.
    def enterInt(self, ctx:AnatomyParser.IntContext):
        pass

    # Exit a parse tree produced by AnatomyParser#int.
    def exitInt(self, ctx:AnatomyParser.IntContext):
        pass


    # Enter a parse tree produced by AnatomyParser#str.
    def enterStr(self, ctx:AnatomyParser.StrContext):
        pass

    # Exit a parse tree produced by AnatomyParser#str.
    def exitStr(self, ctx:AnatomyParser.StrContext):
        pass


    # Enter a parse tree produced by AnatomyParser#abs.
    def enterAbs(self, ctx:AnatomyParser.AbsContext):
        pass

    # Exit a parse tree produced by AnatomyParser#abs.
    def exitAbs(self, ctx:AnatomyParser.AbsContext):
        pass


    # Enter a parse tree produced by AnatomyParser#functionCall.
    def enterFunctionCall(self, ctx:AnatomyParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by AnatomyParser#functionCall.
    def exitFunctionCall(self, ctx:AnatomyParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by AnatomyParser#dfAssign.
    def enterDfAssign(self, ctx:AnatomyParser.DfAssignContext):
        pass

    # Exit a parse tree produced by AnatomyParser#dfAssign.
    def exitDfAssign(self, ctx:AnatomyParser.DfAssignContext):
        pass


    # Enter a parse tree produced by AnatomyParser#transpose.
    def enterTranspose(self, ctx:AnatomyParser.TransposeContext):
        pass

    # Exit a parse tree produced by AnatomyParser#transpose.
    def exitTranspose(self, ctx:AnatomyParser.TransposeContext):
        pass


    # Enter a parse tree produced by AnatomyParser#trigFunction.
    def enterTrigFunction(self, ctx:AnatomyParser.TrigFunctionContext):
        pass

    # Exit a parse tree produced by AnatomyParser#trigFunction.
    def exitTrigFunction(self, ctx:AnatomyParser.TrigFunctionContext):
        pass


    # Enter a parse tree produced by AnatomyParser#rooti.
    def enterRooti(self, ctx:AnatomyParser.RootiContext):
        pass

    # Exit a parse tree produced by AnatomyParser#rooti.
    def exitRooti(self, ctx:AnatomyParser.RootiContext):
        pass


    # Enter a parse tree produced by AnatomyParser#lists.
    def enterLists(self, ctx:AnatomyParser.ListsContext):
        pass

    # Exit a parse tree produced by AnatomyParser#lists.
    def exitLists(self, ctx:AnatomyParser.ListsContext):
        pass


    # Enter a parse tree produced by AnatomyParser#listAppend.
    def enterListAppend(self, ctx:AnatomyParser.ListAppendContext):
        pass

    # Exit a parse tree produced by AnatomyParser#listAppend.
    def exitListAppend(self, ctx:AnatomyParser.ListAppendContext):
        pass


    # Enter a parse tree produced by AnatomyParser#listElement.
    def enterListElement(self, ctx:AnatomyParser.ListElementContext):
        pass

    # Exit a parse tree produced by AnatomyParser#listElement.
    def exitListElement(self, ctx:AnatomyParser.ListElementContext):
        pass


    # Enter a parse tree produced by AnatomyParser#listElementassign.
    def enterListElementassign(self, ctx:AnatomyParser.ListElementassignContext):
        pass

    # Exit a parse tree produced by AnatomyParser#listElementassign.
    def exitListElementassign(self, ctx:AnatomyParser.ListElementassignContext):
        pass


    # Enter a parse tree produced by AnatomyParser#listIndex.
    def enterListIndex(self, ctx:AnatomyParser.ListIndexContext):
        pass

    # Exit a parse tree produced by AnatomyParser#listIndex.
    def exitListIndex(self, ctx:AnatomyParser.ListIndexContext):
        pass


    # Enter a parse tree produced by AnatomyParser#listLen.
    def enterListLen(self, ctx:AnatomyParser.ListLenContext):
        pass

    # Exit a parse tree produced by AnatomyParser#listLen.
    def exitListLen(self, ctx:AnatomyParser.ListLenContext):
        pass


    # Enter a parse tree produced by AnatomyParser#listRemove.
    def enterListRemove(self, ctx:AnatomyParser.ListRemoveContext):
        pass

    # Exit a parse tree produced by AnatomyParser#listRemove.
    def exitListRemove(self, ctx:AnatomyParser.ListRemoveContext):
        pass


    # Enter a parse tree produced by AnatomyParser#listClear.
    def enterListClear(self, ctx:AnatomyParser.ListClearContext):
        pass

    # Exit a parse tree produced by AnatomyParser#listClear.
    def exitListClear(self, ctx:AnatomyParser.ListClearContext):
        pass


    # Enter a parse tree produced by AnatomyParser#listId.
    def enterListId(self, ctx:AnatomyParser.ListIdContext):
        pass

    # Exit a parse tree produced by AnatomyParser#listId.
    def exitListId(self, ctx:AnatomyParser.ListIdContext):
        pass


    # Enter a parse tree produced by AnatomyParser#dicts.
    def enterDicts(self, ctx:AnatomyParser.DictsContext):
        pass

    # Exit a parse tree produced by AnatomyParser#dicts.
    def exitDicts(self, ctx:AnatomyParser.DictsContext):
        pass


    # Enter a parse tree produced by AnatomyParser#dictElement.
    def enterDictElement(self, ctx:AnatomyParser.DictElementContext):
        pass

    # Exit a parse tree produced by AnatomyParser#dictElement.
    def exitDictElement(self, ctx:AnatomyParser.DictElementContext):
        pass


    # Enter a parse tree produced by AnatomyParser#dictElementassign.
    def enterDictElementassign(self, ctx:AnatomyParser.DictElementassignContext):
        pass

    # Exit a parse tree produced by AnatomyParser#dictElementassign.
    def exitDictElementassign(self, ctx:AnatomyParser.DictElementassignContext):
        pass


    # Enter a parse tree produced by AnatomyParser#dictKeys.
    def enterDictKeys(self, ctx:AnatomyParser.DictKeysContext):
        pass

    # Exit a parse tree produced by AnatomyParser#dictKeys.
    def exitDictKeys(self, ctx:AnatomyParser.DictKeysContext):
        pass


    # Enter a parse tree produced by AnatomyParser#dictValues.
    def enterDictValues(self, ctx:AnatomyParser.DictValuesContext):
        pass

    # Exit a parse tree produced by AnatomyParser#dictValues.
    def exitDictValues(self, ctx:AnatomyParser.DictValuesContext):
        pass


    # Enter a parse tree produced by AnatomyParser#dictUpdate.
    def enterDictUpdate(self, ctx:AnatomyParser.DictUpdateContext):
        pass

    # Exit a parse tree produced by AnatomyParser#dictUpdate.
    def exitDictUpdate(self, ctx:AnatomyParser.DictUpdateContext):
        pass


    # Enter a parse tree produced by AnatomyParser#dictItem.
    def enterDictItem(self, ctx:AnatomyParser.DictItemContext):
        pass

    # Exit a parse tree produced by AnatomyParser#dictItem.
    def exitDictItem(self, ctx:AnatomyParser.DictItemContext):
        pass


    # Enter a parse tree produced by AnatomyParser#arrays.
    def enterArrays(self, ctx:AnatomyParser.ArraysContext):
        pass

    # Exit a parse tree produced by AnatomyParser#arrays.
    def exitArrays(self, ctx:AnatomyParser.ArraysContext):
        pass


    # Enter a parse tree produced by AnatomyParser#arrayElement.
    def enterArrayElement(self, ctx:AnatomyParser.ArrayElementContext):
        pass

    # Exit a parse tree produced by AnatomyParser#arrayElement.
    def exitArrayElement(self, ctx:AnatomyParser.ArrayElementContext):
        pass


    # Enter a parse tree produced by AnatomyParser#createDataFrame.
    def enterCreateDataFrame(self, ctx:AnatomyParser.CreateDataFrameContext):
        pass

    # Exit a parse tree produced by AnatomyParser#createDataFrame.
    def exitCreateDataFrame(self, ctx:AnatomyParser.CreateDataFrameContext):
        pass


    # Enter a parse tree produced by AnatomyParser#loadCSV.
    def enterLoadCSV(self, ctx:AnatomyParser.LoadCSVContext):
        pass

    # Exit a parse tree produced by AnatomyParser#loadCSV.
    def exitLoadCSV(self, ctx:AnatomyParser.LoadCSVContext):
        pass


    # Enter a parse tree produced by AnatomyParser#saveCSV.
    def enterSaveCSV(self, ctx:AnatomyParser.SaveCSVContext):
        pass

    # Exit a parse tree produced by AnatomyParser#saveCSV.
    def exitSaveCSV(self, ctx:AnatomyParser.SaveCSVContext):
        pass


    # Enter a parse tree produced by AnatomyParser#columnDataFrame.
    def enterColumnDataFrame(self, ctx:AnatomyParser.ColumnDataFrameContext):
        pass

    # Exit a parse tree produced by AnatomyParser#columnDataFrame.
    def exitColumnDataFrame(self, ctx:AnatomyParser.ColumnDataFrameContext):
        pass


    # Enter a parse tree produced by AnatomyParser#selectRow.
    def enterSelectRow(self, ctx:AnatomyParser.SelectRowContext):
        pass

    # Exit a parse tree produced by AnatomyParser#selectRow.
    def exitSelectRow(self, ctx:AnatomyParser.SelectRowContext):
        pass


    # Enter a parse tree produced by AnatomyParser#filterRows.
    def enterFilterRows(self, ctx:AnatomyParser.FilterRowsContext):
        pass

    # Exit a parse tree produced by AnatomyParser#filterRows.
    def exitFilterRows(self, ctx:AnatomyParser.FilterRowsContext):
        pass


    # Enter a parse tree produced by AnatomyParser#addColumn.
    def enterAddColumn(self, ctx:AnatomyParser.AddColumnContext):
        pass

    # Exit a parse tree produced by AnatomyParser#addColumn.
    def exitAddColumn(self, ctx:AnatomyParser.AddColumnContext):
        pass


    # Enter a parse tree produced by AnatomyParser#dropColumn.
    def enterDropColumn(self, ctx:AnatomyParser.DropColumnContext):
        pass

    # Exit a parse tree produced by AnatomyParser#dropColumn.
    def exitDropColumn(self, ctx:AnatomyParser.DropColumnContext):
        pass


    # Enter a parse tree produced by AnatomyParser#describeDataFrame.
    def enterDescribeDataFrame(self, ctx:AnatomyParser.DescribeDataFrameContext):
        pass

    # Exit a parse tree produced by AnatomyParser#describeDataFrame.
    def exitDescribeDataFrame(self, ctx:AnatomyParser.DescribeDataFrameContext):
        pass


    # Enter a parse tree produced by AnatomyParser#headDataFrame.
    def enterHeadDataFrame(self, ctx:AnatomyParser.HeadDataFrameContext):
        pass

    # Exit a parse tree produced by AnatomyParser#headDataFrame.
    def exitHeadDataFrame(self, ctx:AnatomyParser.HeadDataFrameContext):
        pass


    # Enter a parse tree produced by AnatomyParser#mergeDataFrames.
    def enterMergeDataFrames(self, ctx:AnatomyParser.MergeDataFramesContext):
        pass

    # Exit a parse tree produced by AnatomyParser#mergeDataFrames.
    def exitMergeDataFrames(self, ctx:AnatomyParser.MergeDataFramesContext):
        pass


    # Enter a parse tree produced by AnatomyParser#selectColumn.
    def enterSelectColumn(self, ctx:AnatomyParser.SelectColumnContext):
        pass

    # Exit a parse tree produced by AnatomyParser#selectColumn.
    def exitSelectColumn(self, ctx:AnatomyParser.SelectColumnContext):
        pass


    # Enter a parse tree produced by AnatomyParser#equalsF.
    def enterEqualsF(self, ctx:AnatomyParser.EqualsFContext):
        pass

    # Exit a parse tree produced by AnatomyParser#equalsF.
    def exitEqualsF(self, ctx:AnatomyParser.EqualsFContext):
        pass


    # Enter a parse tree produced by AnatomyParser#minorF.
    def enterMinorF(self, ctx:AnatomyParser.MinorFContext):
        pass

    # Exit a parse tree produced by AnatomyParser#minorF.
    def exitMinorF(self, ctx:AnatomyParser.MinorFContext):
        pass


    # Enter a parse tree produced by AnatomyParser#greaterF.
    def enterGreaterF(self, ctx:AnatomyParser.GreaterFContext):
        pass

    # Exit a parse tree produced by AnatomyParser#greaterF.
    def exitGreaterF(self, ctx:AnatomyParser.GreaterFContext):
        pass


    # Enter a parse tree produced by AnatomyParser#parensF.
    def enterParensF(self, ctx:AnatomyParser.ParensFContext):
        pass

    # Exit a parse tree produced by AnatomyParser#parensF.
    def exitParensF(self, ctx:AnatomyParser.ParensFContext):
        pass


    # Enter a parse tree produced by AnatomyParser#andOrF.
    def enterAndOrF(self, ctx:AnatomyParser.AndOrFContext):
        pass

    # Exit a parse tree produced by AnatomyParser#andOrF.
    def exitAndOrF(self, ctx:AnatomyParser.AndOrFContext):
        pass


    # Enter a parse tree produced by AnatomyParser#complejo.
    def enterComplejo(self, ctx:AnatomyParser.ComplejoContext):
        pass

    # Exit a parse tree produced by AnatomyParser#complejo.
    def exitComplejo(self, ctx:AnatomyParser.ComplejoContext):
        pass


    # Enter a parse tree produced by AnatomyParser#img.
    def enterImg(self, ctx:AnatomyParser.ImgContext):
        pass

    # Exit a parse tree produced by AnatomyParser#img.
    def exitImg(self, ctx:AnatomyParser.ImgContext):
        pass


    # Enter a parse tree produced by AnatomyParser#CosFunc.
    def enterCosFunc(self, ctx:AnatomyParser.CosFuncContext):
        pass

    # Exit a parse tree produced by AnatomyParser#CosFunc.
    def exitCosFunc(self, ctx:AnatomyParser.CosFuncContext):
        pass


    # Enter a parse tree produced by AnatomyParser#SenFunc.
    def enterSenFunc(self, ctx:AnatomyParser.SenFuncContext):
        pass

    # Exit a parse tree produced by AnatomyParser#SenFunc.
    def exitSenFunc(self, ctx:AnatomyParser.SenFuncContext):
        pass


    # Enter a parse tree produced by AnatomyParser#TanFunc.
    def enterTanFunc(self, ctx:AnatomyParser.TanFuncContext):
        pass

    # Exit a parse tree produced by AnatomyParser#TanFunc.
    def exitTanFunc(self, ctx:AnatomyParser.TanFuncContext):
        pass



del AnatomyParser