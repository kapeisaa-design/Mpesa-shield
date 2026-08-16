const API_URL = "http://127.0.0.1:8000";


const messageInput =
    document.getElementById("message");


const analyzeButton =
    document.getElementById("analyzeBtn");


const characterCount =
    document.getElementById("characterCount");


const loading =
    document.getElementById("loading");


const errorBox =
    document.getElementById("error");


const result =
    document.getElementById("result");


const riskCategory =
    document.getElementById("riskCategory");


const riskScore =
    document.getElementById("riskScore");


const reasonsList =
    document.getElementById("reasons");


const recommendationsList =
    document.getElementById("recommendations");



/*
    Update the character counter.
*/

messageInput.addEventListener(
    "input",
    () => {

        characterCount.textContent =
            `${messageInput.value.length} / 2000`;

    }
);



/*
    Clear previous results and errors.
*/

function clearMessages() {

    errorBox.classList.add("hidden");

    errorBox.textContent = "";

    result.classList.add("hidden");

}



/*
    Display an error message.
*/

function showError(message) {

    errorBox.textContent = message;

    errorBox.classList.remove("hidden");

}



/*
    Show or hide loading state.
*/

function showLoading(isLoading) {

    if (isLoading) {

        loading.classList.remove("hidden");

        analyzeButton.disabled = true;

        analyzeButton.textContent =
            "Analyzing...";

    } else { 

        loading.classList.add("hidden");

        analyzeButton.disabled = false;

        analyzeButton.textContent =
            "Analyze message";

    }

}



/*
    Safely convert text into HTML.
    This helps prevent HTML injection.
*/

function escapeHtml(value) {

    const element =
        document.createElement("div");

    element.textContent = value;

    return element.innerHTML;

}



/*
    Convert an array into safe list items.
*/

function createListItems(items) {
    if (!Array.isArray(items)) {
        return "";
    }

    return items
        .map(item => {
            const li = document.createElement("li");
            li.textContent = item;
            return li.outerHTML;
        })
        .join("");
}



/*
    Display API result.
*/

function displayResult(data) {

    riskCategory.textContent =
        data.category;


    riskScore.textContent =
        data.score;


    reasonsList.innerHTML =
        createListItems(data.reasons);


    recommendationsList.innerHTML =
        createListItems(
            data.recommendations
        );


    result.classList.remove("hidden");

}



/*
    Send message to Python API.
*/

async function analyzeMessage() {

    clearMessages();


    const message =
        messageInput.value.trim();


    if (!message) {

        showError(
            "Please enter a message to analyze."
        );

        return;
    }


    showLoading(true);


    try {

        const response =
            await fetch(
                `${API_URL}/analyze`,
                {
                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        message: message
                    })
                }
            );


        const data =
            await response.json();


        if (!response.ok) {

            throw new Error(
                data.detail ||
                "Unable to analyze the message."
            );

        }


        displayResult(data);


    } catch (error) {

        console.error(error);


        showError(
            "The analysis service could not be reached. " +
            "Make sure the Python backend is running."
        );


    } finally {

        showLoading(false);

    }

}



analyzeButton.addEventListener(
    "click",
    analyzeMessage
);