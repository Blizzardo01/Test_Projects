function CalculatorController(input) {
    var me = {};
    var ctr = {};

    var rollingdata = "";

    me.watchEnter = function () {
        $(document).on("click", "button[id^='input']", function () {
            var _clickvalue = $(this).attr("data");

            if (me.IsOperator(_clickvalue)) {
                $("#output").val("Operator Value");
            } else if (me.IsCommand(_clickvalue)) {
                $("#output").val("Command Value");
            } else if (me.IsNumeric(_clickvalue)) {
                rollingdata += _clickvalue;

                $("#output").val(rollingdata);
            } else {
                $("#output").val("Error!");
            }
                
            /*$("#output").val(_clickvalue);*/
        });
    };

    me.IsNumeric = function (input) {
        return $.isNumeric(input);
    }

    me.IsCommand = function (input) {
        if (input === "c" || input === "+-" ||
            input === "%" || input === "." || input === "=")
            return true;

        return false;
    }

    me.IsOperator = function (input) {
        if (input === "-" || input === "+" || input === "/" || input === "*")
            return true;

        return false;
    }



    ctr.intialize = function () {
        me.watchEnter();
    };

    return ctr;
}

$(function () {
    var CController = new CalculatorController();
    CController.intialize();
});