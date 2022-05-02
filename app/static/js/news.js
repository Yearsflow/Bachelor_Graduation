$("input[name='check0']").on('click', function() {
    var a = $("input[name='check0']").val();
    var flag = document.querySelector('input[name="check0"]').checked;
    var data = {
        data: JSON.stringify({
            'id': a,
            'flag': flag
        })
    };
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "/user_index",
        data: data,
        success: function(result) {
            console.log(result)
        },
        error: function(result) {
            console.log(result)
        }
    });
});
$("input[name='check1']").on('click', function() {
    var a = $("input[name='check1']").val();
    var flag = document.querySelector('input[name="check1"]').checked;
    var data = {
        data: JSON.stringify({
            'id': a,
            'flag': flag
        })
    };
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "/user_index",
        data: data,
        success: function(result) {
            console.log(result)
        },
        error: function(result) {
            console.log(result)
        }
    });
});
$("input[name='check2']").on('click', function() {
    var a = $("input[name='check2']").val();
    var flag = document.querySelector('input[name="check2"]').checked;
    var data = {
        data: JSON.stringify({
            'id': a,
            'flag': flag
        })
    };
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "/user_index",
        data: data,
        success: function(result) {
            console.log(result)
        },
        error: function(result) {
            console.log(result)
        }
    });
});
$("input[name='check3']").on('click', function() {
    var a = $("input[name='check3']").val();
    var flag = document.querySelector('input[name="check3"]').checked;
    var data = {
        data: JSON.stringify({
            'id': a,
            'flag': flag
        })
    };
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "/user_index",
        data: data,
        success: function(result) {
            console.log(result)
        },
        error: function(result) {
            console.log(result)
        }
    });
});
$("input[name='check4']").on('click', function() {
    var a = $("input[name='check4']").val();
    var flag = document.querySelector('input[name="check4"]').checked;
    var data = {
        data: JSON.stringify({
            'id': a,
            'flag': flag
        })
    };
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "/user_index",
        data: data,
        success: function(result) {
            console.log(result)
        },
        error: function(result) {
            console.log(result)
        }
    });
});
$("input[name='check0']").on('click', function() {
    var a = $("input[name='check0']").val();
    var flag = document.querySelector('input[name="check0"]').checked;
    var data = {
        data: JSON.stringify({
            'id': a,
            'flag': flag
        })
    };
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "/user_index",
        data: data,
        success: function(result) {
            console.log(result)
        },
        error: function(result) {
            console.log(result)
        }
    });
});