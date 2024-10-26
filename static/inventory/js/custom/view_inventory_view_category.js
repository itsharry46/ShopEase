$(document).ready(function () {
  category_status_label_toggle();
  $("#category_status").on("change", function () {
    category_status_label_toggle();
  });
});

function category_status_label_toggle() {
  const selectedValue = $("#category_status").val();
  const labelElement = document.getElementById("category-status-label");

  if (selectedValue !== "") {
    labelElement.classList.add("floating-label");
  } else {
    labelElement.classList.remove("floating-label");
  }
}

$(function () {
  var s,
    o,
    e = $(".select2"),
    e =
      (e.length &&
        e.each(function () {
          var e = $(this);
          e.wrap('<div class="position-relative"></div>').select2({ dropdownParent: e.parent(), placeholder: e.data("placeholder") });
        }),
      $(".form-repeater"));
  e.length &&
    ((s = 2),
    (o = 1),
    e.on("submit", function (e) {
      e.preventDefault();
    }),
    e.repeater({
      show: function () {
        var a = $(this).find(".form-control, .form-select"),
          t = $(this).find(".form-label");
        a.each(function (e) {
          var r = "form-repeater-" + s + "-" + o;
          $(a[e]).attr("id", r), $(t[e]).attr("for", r), o++;
        }),
          s++,
          $(this).slideDown(),
          $(".select2-container").remove(),
          $(".select2.form-select").select2({ placeholder: "Placeholder text" }),
          $(".select2-container").css("width", "100%"),
          $(".form-repeater:first .form-select").select2({ dropdownParent: $(this).parent(), placeholder: "Placeholder text" }),
          $(".position-relative .select2").each(function () {
            $(this).select2({ dropdownParent: $(this).closest(".position-relative") });
          });
      },
    }));
});

/* Custom Code Starts Here */
document.getElementById("search_category").addEventListener("keyup", function () {
  // Get the value of the search input
  const searchTerm = this.value.toLowerCase();
  const rows = document.querySelectorAll("#DataTables_Table_0 tbody tr");

  rows.forEach((row) => {
    // Get the text content of each cell in the current row
    const cells = row.getElementsByTagName("td");

    let rowVisible = false;

    // Check if any cell contains the search term
    for (let i = 0; i < cells.length; i++) {
      const cell = cells[i];
      if (cell.textContent.toLowerCase().indexOf(searchTerm) > -1) {
        rowVisible = true;
        break; // If a match is found, no need to check further
      }
    }

    // Show or hide the row based on the search term
    row.style.display = rowVisible ? "" : "none";
  });
});
