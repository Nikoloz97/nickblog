// Disables input fields based on content type property

document.addEventListener("DOMContentLoaded", function () {
  const $ = django.jQuery;

  function toggleFields() {
    $(".tabular.inline-related tbody tr").each(function () {
      const $row = $(this);

      if ($row.hasClass("empty-form")) return;

      const $typeSelect = $row.find('[name*="-content_type"]');

      if (!$typeSelect.length) return;

      function updateVisibility() {
        const selected = $typeSelect.val();

        const $headerField = $row.find('[name*="-header"]');
        const $subheaderField = $row.find('[name*="-subheader"]');
        const $textField = $row.find('[name*="-text"]');
        const $linkUrlField = $row.find('[name*="-link_url"]');
        const $linkTextField = $row.find('[name*="-link_text"]');
        const $imageField = $row.find('[name*="-image"]');

        [
          $headerField,
          $subheaderField,
          $textField,
          $linkUrlField,
          $linkTextField,
          $imageField,
        ].forEach(($field) => {
          $field.prop("disabled", true).css({
            "background-color": "#242526",
            color: "#999",
            opacity: "1",
          });
        });

        switch (selected) {
          case "header":
            $headerField.prop("disabled", false).css({
              "background-color": "",
              color: "",
              opacity: "",
            });
            break;
          case "subheader":
            $subheaderField.prop("disabled", false).css({
              "background-color": "",
              color: "",
              opacity: "",
            });
            break;
          case "text":
            $textField.prop("disabled", false).css({
              "background-color": "",
              color: "",
              opacity: "",
            });
            break;
          case "link":
            $linkUrlField.prop("disabled", false).css({
              "background-color": "",
              color: "",
              opacity: "",
            });
            $linkTextField.prop("disabled", false).css({
              "background-color": "",
              color: "",
              opacity: "",
            });
            break;
          case "image":
            $imageField.prop("disabled", false).css({
              "background-color": "",
              color: "",
              opacity: "",
            });
            break;
        }
      }

      $typeSelect.on("change", updateVisibility);
      updateVisibility();
    });
  }

  toggleFields();

  $(document).on("formset:added", function (event, $row) {
    console.log("New form added, applying field toggle");
    toggleFields();
  });
});
