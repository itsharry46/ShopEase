// Clear error response for add category
function clearAddCategoryErrors() {
  const clearErrors = ["category_name_error", "category_description_error", "category_status_error"];

  for (let index = 0; index < clearErrors.length; index++) {
    document.getElementById(clearErrors[index]).textContent = "";
  }
}

// Clear success response for add category
const initialOpen = document.getElementById("addCategoryList");
initialOpen.addEventListener("click", function () {
  document.getElementById("add_category_response").textContent = "";
  document.getElementById("category_name").value = "";
  document.getElementById("category_description").value = "";

  $("#category_status").select2("val", "Y");
});

// AJAX Request for add category
const add_category = document.getElementById("submit_add_category");
add_category.addEventListener("click", function (event) {
  event.preventDefault();
  clearAddCategoryErrors();

  var ajax_data = {
    category_name: document.getElementById("category_name").value,
    category_description: document.getElementById("category_description").value,
    category_status: document.getElementById("category_status").value,
    csrfmiddlewaretoken: commonGetCSRFToken(), // Include CSRF token
  };

  $.ajax({
    url: "add_category",
    type: "POST",
    data: ajax_data,
    success: function (response) {
      console.log(response);
      document.getElementById("add_category_response").innerText = response.message;
    },
    error: function (xhr) {
      const errors = xhr.responseJSON;

      for (let index = 0; index < Object.keys(errors).length; index++) {
        document.getElementById(`${Object.keys(errors)[index]}_error`).textContent = Object.values(errors)[index];
      }
    },
  });
});

// Reset for add category
const reset_category = document.getElementById("reset_add_category");
reset_category.addEventListener("click", function () {
  clearAddCategoryErrors();
});
