#!/bin/bash
zowe zos-jobs submit data-set "fzoi.oapi.jcl(oapipath)" --wfo
zowe zos-files download data-set "fzoi.test.pathout" --encoding 1140 -f './static/openapispec/pathout.json'

