$(document).ready(function () {
  $("#product_category").on("change", function () {
    product_listing_filters("product_category", "product-category-label");
  });

  $("#product_status").on("change", function () {
    product_listing_filters("product_status", "category-status-label");
  });

  $("#product_stock_status").on("change", function () {
    product_listing_filters("product_stock_status", "product-stock-status-label");
  });
});

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
        a.each(function (index) {
          var r = "form-repeater-" + s + "-" + o;
          // Check if the ID already exists
          if ($("#" + r).length === 0) {
            $(a[index]).attr("id", r);
            $(t[index]).attr("for", r);
            o++;
          } else {
            // Optionally handle the case where the ID already exists
            console.warn("ID already exists: " + r);
          }
        });
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

function product_listing_filters(filter_name, label_name) {
  const selectedValue = document.getElementById(filter_name).value;
  const labelElement = document.getElementById(label_name);

  if (selectedValue !== "0") {
    labelElement.removeAttribute("hidden");
    labelElement.classList.add("floating-label");
  } else {
    labelElement.setAttribute("hidden", true);
    labelElement.classList.remove("floating-label");
  }
}
