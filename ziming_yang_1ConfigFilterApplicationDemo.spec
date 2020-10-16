/*
A KBase module: ziming_yang_1ConfigFilterApplicationDemo
This sample module contains one small method that filters contigs.
*/

module ziming_yang_1ConfigFilterApplicationDemo {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_ziming_yang_1ConfigFilterApplicationDemo(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
