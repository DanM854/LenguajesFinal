# Generated from Anatomy.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .AnatomyParser import AnatomyParser
else:
    from AnatomyParser import AnatomyParser

# This class defines a complete generic visitor for a parse tree produced by AnatomyParser.

class AnatomyVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AnatomyParser#program.
    def visitProgram(self, ctx:AnatomyParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#expression.
    def visitExpression(self, ctx:AnatomyParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#statement.
    def visitStatement(self, ctx:AnatomyParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#show.
    def visitShow(self, ctx:AnatomyParser.ShowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#control.
    def visitControl(self, ctx:AnatomyParser.ControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#function.
    def visitFunction(self, ctx:AnatomyParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#fileOp.
    def visitFileOp(self, ctx:AnatomyParser.FileOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#blank.
    def visitBlank(self, ctx:AnatomyParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#assign.
    def visitAssign(self, ctx:AnatomyParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#functionStatement.
    def visitFunctionStatement(self, ctx:AnatomyParser.FunctionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#parametros.
    def visitParametros(self, ctx:AnatomyParser.ParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#args.
    def visitArgs(self, ctx:AnatomyParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#structureControl.
    def visitStructureControl(self, ctx:AnatomyParser.StructureControlContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#if.
    def visitIf(self, ctx:AnatomyParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#ifElse.
    def visitIfElse(self, ctx:AnatomyParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#while.
    def visitWhile(self, ctx:AnatomyParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#for.
    def visitFor(self, ctx:AnatomyParser.ForContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#read.
    def visitRead(self, ctx:AnatomyParser.ReadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#printExpr.
    def visitPrintExpr(self, ctx:AnatomyParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#graph.
    def visitGraph(self, ctx:AnatomyParser.GraphContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#graphType.
    def visitGraphType(self, ctx:AnatomyParser.GraphTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#graphParams.
    def visitGraphParams(self, ctx:AnatomyParser.GraphParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#openFile.
    def visitOpenFile(self, ctx:AnatomyParser.OpenFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#closeFile.
    def visitCloseFile(self, ctx:AnatomyParser.CloseFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#writeFile.
    def visitWriteFile(self, ctx:AnatomyParser.WriteFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#deleteFile.
    def visitDeleteFile(self, ctx:AnatomyParser.DeleteFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#readingFile.
    def visitReadingFile(self, ctx:AnatomyParser.ReadingFileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#readLine.
    def visitReadLine(self, ctx:AnatomyParser.ReadLineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#readAll.
    def visitReadAll(self, ctx:AnatomyParser.ReadAllContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#Logic.
    def visitLogic(self, ctx:AnatomyParser.LogicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#Aritmetic.
    def visitAritmetic(self, ctx:AnatomyParser.AritmeticContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#return.
    def visitReturn(self, ctx:AnatomyParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#idL.
    def visitIdL(self, ctx:AnatomyParser.IdLContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#andOr.
    def visitAndOr(self, ctx:AnatomyParser.AndOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#negation.
    def visitNegation(self, ctx:AnatomyParser.NegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#minor.
    def visitMinor(self, ctx:AnatomyParser.MinorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#bool.
    def visitBool(self, ctx:AnatomyParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#parensL.
    def visitParensL(self, ctx:AnatomyParser.ParensLContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#equals.
    def visitEquals(self, ctx:AnatomyParser.EqualsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#equalsL.
    def visitEqualsL(self, ctx:AnatomyParser.EqualsLContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#greater.
    def visitGreater(self, ctx:AnatomyParser.GreaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#parens.
    def visitParens(self, ctx:AnatomyParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#arrayAssign.
    def visitArrayAssign(self, ctx:AnatomyParser.ArrayAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#dot.
    def visitDot(self, ctx:AnatomyParser.DotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#float.
    def visitFloat(self, ctx:AnatomyParser.FloatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#mulDiv.
    def visitMulDiv(self, ctx:AnatomyParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#listAssign.
    def visitListAssign(self, ctx:AnatomyParser.ListAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#negative.
    def visitNegative(self, ctx:AnatomyParser.NegativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#split.
    def visitSplit(self, ctx:AnatomyParser.SplitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#root.
    def visitRoot(self, ctx:AnatomyParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#hex.
    def visitHex(self, ctx:AnatomyParser.HexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#id.
    def visitId(self, ctx:AnatomyParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#dictAssign.
    def visitDictAssign(self, ctx:AnatomyParser.DictAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#power.
    def visitPower(self, ctx:AnatomyParser.PowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#comp.
    def visitComp(self, ctx:AnatomyParser.CompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#modDivent.
    def visitModDivent(self, ctx:AnatomyParser.ModDiventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#cross.
    def visitCross(self, ctx:AnatomyParser.CrossContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#castInt.
    def visitCastInt(self, ctx:AnatomyParser.CastIntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#addSub.
    def visitAddSub(self, ctx:AnatomyParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#reverse.
    def visitReverse(self, ctx:AnatomyParser.ReverseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#int.
    def visitInt(self, ctx:AnatomyParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#str.
    def visitStr(self, ctx:AnatomyParser.StrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#abs.
    def visitAbs(self, ctx:AnatomyParser.AbsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#functionCall.
    def visitFunctionCall(self, ctx:AnatomyParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#dfAssign.
    def visitDfAssign(self, ctx:AnatomyParser.DfAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#transpose.
    def visitTranspose(self, ctx:AnatomyParser.TransposeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#trigFunction.
    def visitTrigFunction(self, ctx:AnatomyParser.TrigFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#rooti.
    def visitRooti(self, ctx:AnatomyParser.RootiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#lists.
    def visitLists(self, ctx:AnatomyParser.ListsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#listAppend.
    def visitListAppend(self, ctx:AnatomyParser.ListAppendContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#listElement.
    def visitListElement(self, ctx:AnatomyParser.ListElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#listElementassign.
    def visitListElementassign(self, ctx:AnatomyParser.ListElementassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#listIndex.
    def visitListIndex(self, ctx:AnatomyParser.ListIndexContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#listLen.
    def visitListLen(self, ctx:AnatomyParser.ListLenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#listRemove.
    def visitListRemove(self, ctx:AnatomyParser.ListRemoveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#listClear.
    def visitListClear(self, ctx:AnatomyParser.ListClearContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#listId.
    def visitListId(self, ctx:AnatomyParser.ListIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#dicts.
    def visitDicts(self, ctx:AnatomyParser.DictsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#dictElement.
    def visitDictElement(self, ctx:AnatomyParser.DictElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#dictElementassign.
    def visitDictElementassign(self, ctx:AnatomyParser.DictElementassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#dictKeys.
    def visitDictKeys(self, ctx:AnatomyParser.DictKeysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#dictValues.
    def visitDictValues(self, ctx:AnatomyParser.DictValuesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#dictUpdate.
    def visitDictUpdate(self, ctx:AnatomyParser.DictUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#dictItem.
    def visitDictItem(self, ctx:AnatomyParser.DictItemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#arrays.
    def visitArrays(self, ctx:AnatomyParser.ArraysContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#arrayElement.
    def visitArrayElement(self, ctx:AnatomyParser.ArrayElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#createDataFrame.
    def visitCreateDataFrame(self, ctx:AnatomyParser.CreateDataFrameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#loadCSV.
    def visitLoadCSV(self, ctx:AnatomyParser.LoadCSVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#saveCSV.
    def visitSaveCSV(self, ctx:AnatomyParser.SaveCSVContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#columnDataFrame.
    def visitColumnDataFrame(self, ctx:AnatomyParser.ColumnDataFrameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#selectRow.
    def visitSelectRow(self, ctx:AnatomyParser.SelectRowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#filterRows.
    def visitFilterRows(self, ctx:AnatomyParser.FilterRowsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#addColumn.
    def visitAddColumn(self, ctx:AnatomyParser.AddColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#dropColumn.
    def visitDropColumn(self, ctx:AnatomyParser.DropColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#describeDataFrame.
    def visitDescribeDataFrame(self, ctx:AnatomyParser.DescribeDataFrameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#headDataFrame.
    def visitHeadDataFrame(self, ctx:AnatomyParser.HeadDataFrameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#mergeDataFrames.
    def visitMergeDataFrames(self, ctx:AnatomyParser.MergeDataFramesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#selectColumn.
    def visitSelectColumn(self, ctx:AnatomyParser.SelectColumnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#equalsF.
    def visitEqualsF(self, ctx:AnatomyParser.EqualsFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#minorF.
    def visitMinorF(self, ctx:AnatomyParser.MinorFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#greaterF.
    def visitGreaterF(self, ctx:AnatomyParser.GreaterFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#parensF.
    def visitParensF(self, ctx:AnatomyParser.ParensFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#andOrF.
    def visitAndOrF(self, ctx:AnatomyParser.AndOrFContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#complejo.
    def visitComplejo(self, ctx:AnatomyParser.ComplejoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#img.
    def visitImg(self, ctx:AnatomyParser.ImgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#CosFunc.
    def visitCosFunc(self, ctx:AnatomyParser.CosFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#SenFunc.
    def visitSenFunc(self, ctx:AnatomyParser.SenFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AnatomyParser#TanFunc.
    def visitTanFunc(self, ctx:AnatomyParser.TanFuncContext):
        return self.visitChildren(ctx)



del AnatomyParser