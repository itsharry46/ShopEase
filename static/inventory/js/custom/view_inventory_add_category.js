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
  document.getElementById("hidden_category_id").value = "";

  document.getElementById("submit_add_category").style.removeProperty("display");
  document.getElementById("submit_update_category").style.setProperty("display", "none", "important");

  $("#category_status").select2("val", "Y");
});

// AJAX Request for add category
const add_category = document.getElementById("submit_add_category");
add_category.addEventListener("click", function (event) {
  event.preventDefault();
  clearAddCategoryErrors();

  var fetch_data = {
    category_name: document.getElementById("category_name").value,
    category_description: document.getElementById("category_description").value,
    category_status: document.getElementById("category_status").value,
    csrfmiddlewaretoken: commonGetCSRFToken(), // Include CSRF token
  };

  fetch("add_category", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": commonGetCSRFToken(), // Include CSRF token
    },
    body: JSON.stringify(fetch_data),
  })
    .then((response) => {
      if (!response.ok) {
        return response.json().then((errors) => {
          throw errors;
        });
      }
      return response.json();
    })
    .then((data) => {
      document.getElementById("add_category_response").innerText = data.message;
    })
    .catch((errors) => {
      for (let key in errors) {
        if (errors.hasOwnProperty(key)) {
          document.getElementById(`${key}_error`).textContent = errors[key];
        }
      }
    });
});

// AJAX Request for update categroy
const update_category = document.getElementById("submit_update_category");
update_category.addEventListener("click", function (event) {
  event.preventDefault();
  clearAddCategoryErrors();

  var fetch_data = {
    category_id: document.getElementById("hidden_category_id").value,
    category_name: document.getElementById("category_name").value,
    category_description: document.getElementById("category_description").value,
    category_status: document.getElementById("category_status").value,
    csrfmiddlewaretoken: commonGetCSRFToken(), // Include CSRF token
  };

  fetch("update_category", {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": commonGetCSRFToken(), // Include CSRF token
    },
    body: JSON.stringify(fetch_data),
  })
    .then((response) => {
      if (!response.ok) {
        return response.json().then((errors) => {
          throw errors;
        });
      }
      return response.json();
    })
    .then((data) => {
      document.getElementById("add_category_response").innerText = data.message;
    })
    .catch((errors) => {
      for (let key in errors) {
        if (errors.hasOwnProperty(key)) {
          document.getElementById(`${key}_error`).textContent = errors[key];
        }
      }
    });
});

// Reset for add category
const reset_category = document.getElementById("reset_add_category");
reset_category.addEventListener("click", function () {
  clearAddCategoryErrors();
});
