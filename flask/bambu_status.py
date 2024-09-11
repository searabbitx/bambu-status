from marshmallow import Schema, fields, post_load
from pathlib import Path
from dummy_data import dummy_data
import json


class BambuStatus:
    def __init__(self, amsHumidity, amsTemp, bedTemper, bedTargetTemper,
                 chamberTemper, failReason, mcPercent, gcodeState, mcPrintErrorCode,
                 mcRemainingTime, nozzleTargetTemper, nozzleTemper, printError, subtask_name):
        self.amsHumidity = amsHumidity
        self.amsTemp = amsTemp
        self.bedTemper = bedTemper
        self.bedTargetTemper = bedTargetTemper
        self.chamberTemper = chamberTemper
        self.failReason = failReason
        self.mcPercent = mcPercent
        self.gcodeState = gcodeState
        self.mcPrintErrorCode = mcPrintErrorCode
        self.mcRemainingTime = mcRemainingTime
        self.nozzleTargetTemper = nozzleTargetTemper
        self.nozzleTemper = nozzleTemper
        self.printError = printError
        self.subtask_name = subtask_name

    def store(self):
        status_dict = BambuStatusSchema().dump(self)
        status_text = json.dumps(status_dict)
        Path('data/status.json').write_text(status_text)

    @staticmethod
    def load():
        try:
            status_text = Path('data/status.json').read_text()
        except FileNotFoundError:
            return dummy_data
        status_dict = json.loads(status_text)
        return BambuStatusSchema().load(status_dict)


class BambuStatusSchema(Schema):
    amsHumidity = fields.String(required=True)
    amsTemp = fields.String(required=True)
    bedTemper = fields.String(required=True)
    bedTargetTemper = fields.String(required=True)
    chamberTemper = fields.String(required=True)
    failReason = fields.String(required=True)
    mcPercent = fields.String(required=True)
    gcodeState = fields.String(required=True)
    mcPrintErrorCode = fields.String(required=True)
    mcRemainingTime = fields.String(required=True)
    nozzleTargetTemper = fields.String(required=True)
    nozzleTemper = fields.String(required=True)
    printError = fields.String(required=True)
    subtask_name = fields.String(required=True)

    @post_load
    def make_bs(self, data, **kwargs):
        return BambuStatus(**data)
