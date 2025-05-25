from flask import Flask, render_template, request, send_file
from docx import Document
import io, os

app = Flask(__name__)

# Map each placeholder in your template to a form field name
PLACEHOLDERS = {
    "[hotel_entity_name]":       "hotel_entity_name",
    "[influencer_name]":         "influencer_name",
    "[nights]":                  "nights",
    "[accommodation_dates]":     "accommodation_dates",
    "[room_types]":              "room_types",
    "[check_in_time]":           "check_in_time",
    "[check_in_date]":           "check_in_date",
    "[check_out_time]":          "check_out_time",
    "[check_out_date]":          "check_out_date",
    "[social_media_handles]":    "social_media_handles",
    "[term_dates]":              "term_dates",
    "[hotel_name]":              "hotel_name",
    "[hotel_address]":           "hotel_address",
    "[program_name]":            "program_name",
    "[min_posts_per_day]":       "min_posts_per_day",
    "[pre_post_days]":           "pre_post_days",
    "[hotel_handle]":            "hotel_handle",
    "[brand_handle]":            "brand_handle",
    "[company_handle]":          "company_handle",
    "[campaign_hashtag]":        "campaign_hashtag",
    "[NUMBER]":                  "conf_years"
}

@app.route("/", methods=["GET"])
def form():
    return render_template("form.html")

@app.route("/generate", methods=["POST"])
def generate():
    # 1) load your master template
    tpl_path = os.path.join(os.path.dirname(__file__),
                            "Influencer_Agreement_Template.docx")
    doc = Document(tpl_path)

    # 2) collect form data
    data = {ph: request.form[field] for ph, field in PLACEHOLDERS.items()}

    # 3) define a robust replace function
    def replace_placeholders_in_paragraph(para):
        text = para.text
        # only proceed if any placeholder is present
        if any(ph in text for ph in PLACEHOLDERS):
            # perform all replacements on the full text
            for ph, field in PLACEHOLDERS.items():
                text = text.replace(ph, data[ph])
            # clear existing runs
            for run in para.runs:
                run._element.getparent().remove(run._element)
            # add one new run with the replaced text
            para.add_run(text)

    # 4) apply to all parts of the doc
    # 4a) body paragraphs
    for para in doc.paragraphs:
        replace_placeholders_in_paragraph(para)
    # 4b) tables in body
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for para in cell.paragraphs:
                    replace_placeholders_in_paragraph(para)
    # 4c) headers & footers
    for section in doc.sections:
        for hdr in (section.header, section.footer):
            for para in hdr.paragraphs:
                replace_placeholders_in_paragraph(para)
            for table in hdr.tables:
                for row in table.rows:
                    for cell in row.cells:
                        for para in cell.paragraphs:
                            replace_placeholders_in_paragraph(para)

    # 5) stream it back
    virtual_doc = io.BytesIO()
    doc.save(virtual_doc)
    virtual_doc.seek(0)
    return send_file(
        virtual_doc,
        as_attachment=True,
        download_name="Influencer_Agreement_Filled.docx",
        mimetype=(
          "application/vnd.openxmlformats-"
          "officedocument.wordprocessingml.document"
        )
    )

if __name__ == "__main__":
    app.run(debug=True)
