$(document).ready(function () {
  console.log("hi");
  $("#events").DataTable({
    order: [[3, "asc"]],
    aoColumns: [
      null,
      null,
      null,
      { sType: "date-uk" },
      { sType: "date-uk" },
      null,
    ],
  });
  $("#hotels").DataTable();
});
jQuery.extend(jQuery.fn.dataTableExt.oSort, {
  "date-uk-pre": function (a) {
    var ukDatea = a.split("/");
    return (ukDatea[2] + ukDatea[1] + ukDatea[0]) * 1;
  },

  "date-uk-asc": function (a, b) {
    return a < b ? -1 : a > b ? 1 : 0;
  },

  "date-uk-desc": function (a, b) {
    return a < b ? 1 : a > b ? -1 : 0;
  },
});

function getCookie(c_name) {
  if (document.cookie.length > 0) {
    c_start = document.cookie.indexOf(c_name + "=");
    if (c_start != -1) {
      c_start = c_start + c_name.length + 1;
      c_end = document.cookie.indexOf(";", c_start);
      if (c_end == -1) c_end = document.cookie.length;
      return unescape(document.cookie.substring(c_start, c_end));
    }
  }
  return "";
}

const getHotelId = (hotel) => {
  console.log(hotel.id);
  var form = document.createElement("form");
  form.method = "POST";
  form.action = "hotelinfo";
  var idInput = document.createElement("input");
  idInput.value = hotel.id;
  idInput.type = "hidden";
  idInput.name = "id";
  var inputElem = document.createElement("input");
  inputElem.type = "hidden";
  inputElem.name = "csrfmiddlewaretoken";
  inputElem.value = getCookie("csrftoken");
  form.appendChild(idInput);
  form.appendChild(inputElem);
  document.body.appendChild(form);
  form.submit();
};

const convertDate = (start) => {
  var x = new Date(start);
  var date = x.getDate();
  var month = x.getMonth(); //Be careful! January is 0 not 1
  var year = x.getFullYear();
  console.log(date + "/" + (month + 1) + "/" + year);
  return date + "/" + (month + 1) + "/" + year;
};

const openModal = (hotel) => {
  $("#fromDate").val(hotel[6].slice(0, 10));
  $("#toDate").val(hotel[7].slice(0, 10));
  $("#event-name").html(hotel[1]);

  console.log(hotel);
  $("#hotelInfoModal").modal("show");
  $("#event-type").html(`${hotel[8]}`);
  $("#event-impact").html(`${hotel[9]}`);
};

const increasePrice = () => {
  var form = document.createElement("form");
  form.method = "POST";
  form.action = "increaseroomprice";
  // id
  var id = document.getElementById("hotelId")
  var name = document.getElementById("event-name")
  var start = document.getElementById("fromDate")
  var end = document.getElementById("toDate")
  var incerease = document.getElementById("price-increase-percentage")
  var inputElem = document.createElement("input");
  var nameInput = document.createElement("input")
  nameInput.value = name.innerHTML

  nameInput.name = "name"
  inputElem.type = "hidden";
  inputElem.name = "csrfmiddlewaretoken";
  inputElem.value = getCookie("csrftoken");
  form.appendChild(id)
  form.appendChild(start)
  form.appendChild(end)
  form.appendChild(incerease)
  form.appendChild(nameInput);
  form.appendChild(inputElem);

  document.body.appendChild(form);
  form.submit();



}


setTimeout(fade_out, 3000);
    function fade_out() {
        $(".message").fadeOut().empty();
    }