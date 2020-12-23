$('#salavat-btn').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#salavat-btn').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'s',
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#salavat-count').text(data['count'])
            }
        }
    });
});

$('#fatehe-btn').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#fatehe-btn').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'f'
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#fatehe-count').text(data['count'])
            }
        }
    });
});

$('#arbain-btn').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#arbain-btn').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'ar'
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#arbain-count').text(data['count'])
            }
        }
    });
});

$('#ashora-btn').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#ashora-btn').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'ash'
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#ashora-count').text(data['count'])
            }
        }
    });
});

$('#btn-joz1').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz1').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j1',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz1-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz2').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz2').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j2',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz2-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz3').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz3').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j3',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz3-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz4').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz4').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j4',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz4-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz5').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz5').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j5',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz5-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz6').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz6').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j6',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz6-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz7').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz7').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j7',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz7-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz8').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz8').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j8',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz8-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz9').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz9').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j9',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz9-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz10').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz10').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j10',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz10-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz11').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz11').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j11',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz11-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz12').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz12').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j12',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz12-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz13').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz13').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j13',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz13-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz14').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz14').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j14',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz14-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz15').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz15').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j15',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz15-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz16').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz16').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j16',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz16-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz17').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz17').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j17',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz17-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz18').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz18').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j18',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz18-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz19').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz19').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j19',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz19-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz20').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz20').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j20',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz20-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz21').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz21').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j21',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz21-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz22').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz22').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j22',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz22-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz23').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz23').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j23',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz23-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz24').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz24').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j24',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz24-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz25').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz25').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j25',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz25-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz26').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz26').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j26',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz26-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz27').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz27').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j27',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz27-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz28').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz28').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j28',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz28-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz29').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz29').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j29',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz29-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});

$('#btn-joz30').click(function () {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    var url = '/vote/'
    var marhom_id = $('#btn-joz30').attr('data-id')

    $.ajax({

        url: url,
        method: 'POST',
        data: {
            'marhom_id': marhom_id,
            'btn':'j30',
            'quran': 1,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $('#joz30-count').text(data['count'])
            }
            if(data['quranStatus'] === 1){
                $('#khatm-count').text(data['khatm'])
                $('#offer').text(data['offer'])
            }
        }
    });
});




