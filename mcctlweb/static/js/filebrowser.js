//$("#grid-keep-selection").bootgrid({
//    ajax: true,
//    post: function () {
//        /* To accumulate custom parameter with the request object */
//        return {
//            id: "b0df282a-0d67-40e5-8558-c9e93b7befed"
//        };
//    },
//    url: "/file-browser/id",
//    //selection: true,
//    //multiSelect: true,
//    //rowSelect: true,
//    //keepSelection: true,
//    formatters: {
//        "link": function (column, row) {
//            $
//            return "<a href=\"#\">" + column.id + ": " + row.id + "</a>";
//        }
//    }
//}).on("selected.rs.jquery.bootgrid", function (e, rows) {
//    var rowIds = [];
//    for (var i = 0; i < rows.length; i++) {
//        rowIds.push(rows[i].id);
//    }
//    //alert("Select: " + rowIds.join(","));
//}).on("deselected.rs.jquery.bootgrid", function (e, rows) {
//    var rowIds = [];
//    for (var i = 0; i < rows.length; i++) {
//        rowIds.push(rows[i].id);
//    }
//    //alert("Deselect: " + rowIds.join(","));
//});
var grid = $("#grid-data").bootgrid({
    ajax: true,
    post: function ()
    {
        return {
            id: "b0df282a-0d67-40e5-8558-c9e93b7befed"
        };
    },
    url: "/file-browser/id",
    formatters: {
        "commands": function(column, row)
        {
            return "<button type=\"button\" class=\"btn btn-xs btn-default command-edit\" data-row-id=\"" + row.name + "\"><span class=\"fa fa-pencil\"></span></button> " +
                "<button type=\"button\" class=\"btn btn-xs btn-default command-delete\" data-row-id=\"" + row.name + "\"><span class=\"fa fa-trash-o\"></span></button>";
        }
    }
}).on("loaded.rs.jquery.bootgrid", function()
{
    /* Executes after data is loaded and rendered */
    grid.find(".command-edit").on("click", function(e)
    {
        alert("You pressed edit on row: " + $(this).data("row-id"));
    }).end().find(".command-delete").on("click", function(e)
    {
        alert("You pressed delete on row: " + $(this).data("row-id"));
    });
});

$('#grid-data-footer').hide();