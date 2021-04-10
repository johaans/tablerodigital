$(function () {
    $('.select2').select2({
        theme: "bootstrap4",
        language: 'es',
        placeholder: 'Buscar..'
    });
    $('form').on('submit', function (e) {
            e.preventDefault();
            var parameters = new FormData(this);



            submit_with_ajax(window.location.pathname, 'Notificación',
            '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
                    location.href = '/erp/product/list/';
            });
    });
});