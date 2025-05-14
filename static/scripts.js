// const startSpeechRecognitionButton = document.getElementById('startSpeechRecognition');
// const transcriptionDiv = document.getElementById('transcription');

// startSpeechRecognitionButton.addEventListener('click', startSpeechRecognition);

// function startSpeechRecognition() {
//   const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
//   recognition.lang = 'en-US';
//   recognition.onstart = function () {
//     startSpeechRecognitionButton.textContent = 'Listening...';
//     startSpeechRecognitionButton.disabled = true;
//   };
//   recognition.onresult = function (event) {
//     const result = event.results[0][0].transcript;
//     transcriptionDiv.textContent = result;
//   };
//   recognition.onend = function () {
//     startSpeechRecognitionButton.textContent = 'Start Speech Recognition';
//     startSpeechRecognitionButton.disabled = false;
//   };
//   recognition.start();
// }

// document.querySelectorAll('.modal').forEach(modal => {
//   let triggerElement = null;

//   modal.addEventListener('show.bs.modal', (event) => {
//     triggerElement = event.relatedTarget;
//   });

//   modal.addEventListener('hide.bs.modal', () => {
//     if (triggerElement) {
//       triggerElement.focus();
//     }
//   });

//   modal.addEventListener('hidden.bs.modal', () => {
//     if (triggerElement && document.activeElement !== triggerElement) {
//       triggerElement.focus();
//     }
//     triggerElement = null;
//   });
// });

// function initMap() {
//   console.log("initMap called");

//   const hospitalDataDiv = document.getElementById('hospital-data');
//   if (!hospitalDataDiv) {
//     console.error("hospital-data div not found");
//     return;
//   }

//   // Parse the data with detailed error handling
//   let showHospitals = false;
//   let staticHospitals = [];
//   let predictedDisease = "";

//   try {
//     const rawShowHospitals = hospitalDataDiv.dataset.showHospitals;
//     showHospitals = rawShowHospitals ? JSON.parse(rawShowHospitals) : false;
//     console.log("Parsed showHospitals:", showHospitals);
//   } catch (error) {
//     console.error("Error parsing data-show-hospitals:", error, "Raw value:", hospitalDataDiv.dataset.showHospitals);
//   }

//   try {
//     const rawStaticHospitals = hospitalDataDiv.dataset.staticHospitals;
//     staticHospitals = rawStaticHospitals ? JSON.parse(rawStaticHospitals) : [];
//     console.log("Parsed staticHospitals:", staticHospitals);
//   } catch (error) {
//     console.error("Error parsing data-static-hospitals:", error, "Raw value:", hospitalDataDiv.dataset.staticHospitals);
//   }

//   try {
//     const rawPredictedDisease = hospitalDataDiv.dataset.predictedDisease;
//     predictedDisease = rawPredictedDisease ? JSON.parse(rawPredictedDisease) : "";
//     console.log("Parsed predictedDisease:", predictedDisease);
//   } catch (error) {
//     console.error("Error parsing data-predicted-disease:", error, "Raw value:", hospitalDataDiv.dataset.predictedDisease);
//   }

//   console.log("Raw data-show-hospitals:", hospitalDataDiv.dataset.showHospitals);
//   console.log("Raw data-static-hospitals:", hospitalDataDiv.dataset.staticHospitals);
//   console.log("Raw data-predicted-disease:", hospitalDataDiv.dataset.predictedDisease);

//   // Set window.staticHospitals if staticHospitals is an array and has data
//   window.staticHospitals = Array.isArray(staticHospitals) && staticHospitals.length > 0 ? staticHospitals : [];
//   window.disease = typeof predictedDisease === 'string' && predictedDisease ? predictedDisease : "";

//   console.log("Static Hospitals (initial):", window.staticHospitals);
//   console.log("Predicted Disease:", window.disease);

//   let searchTerm = 'hospitals';
//   if (window.disease.toLowerCase().includes('heart attack')) {
//     searchTerm = 'heart hospitals';
//   } else if (window.disease.toLowerCase().includes('allergy')) {
//     searchTerm = 'allergy clinics';
//   }

//   const hospitalList = document.getElementById('hospital-list');
//   if (!hospitalList) {
//     console.error("hospital-list element not found");
//     return;
//   }

//   console.log("Rendering static hospitals directly in initMap");
//   renderStaticHospitals(hospitalList, searchTerm);
// }

// function renderStaticHospitals(hospitalList, searchTerm) {
//   console.log("renderStaticHospitals called with hospitals:", window.staticHospitals);
//   hospitalList.innerHTML = ''; // Clear the "Loading..." message
//   if (window.staticHospitals.length > 0) {
//     window.staticHospitals.forEach((hospital, index) => {
//       console.log("Rendering static hospital:", hospital);
//       const facilityCard = document.createElement('div');
//       facilityCard.className = 'hospital-card';
//       facilityCard.innerHTML = `
//         <h5>${escapeHTML(hospital.name)}</h5>
//         <p><em>Specialty: ${escapeHTML(hospital.specialty)}</em></p>
//         <p>Address: ${escapeHTML(hospital.address)}</p>
//         <button class="show-details-btn" data-index="${index}" data-name="${escapeHTML(hospital.name)}" data-address="${escapeHTML(hospital.address)}" data-specialty="${escapeHTML(hospital.specialty)}" data-phone="${escapeHTML(hospital.phone)}" data-website="${escapeHTML(hospital.website)}">Show Details</button>
//         <div id="details-${index}" class="details-space"></div>
//       `;
//       hospitalList.appendChild(facilityCard);
//     });

//     document.querySelectorAll('.show-details-btn').forEach(button => {
//       button.addEventListener('click', () => {
//         const index = button.getAttribute('data-index');
//         const name = button.getAttribute('data-name');
//         const address = button.getAttribute('data-address');
//         const specialty = button.getAttribute('data-specialty');
//         const phone = button.getAttribute('data-phone');
//         const website = button.getAttribute('data-website');
//         showDetails(index, name, address, specialty, phone, website);
//       });
//     });
//   } else {
//     hospitalList.innerHTML =
//     //   `<p>No ${searchTerm} found in static data. Please try again or search on <a href="https://www.google.com/maps/search/${searchTerm}+near+me" target="_blank">Google Maps</a>.</p>`;
//             `<p><a href="https://www.google.com/maps/search/${searchTerm}+near+me" target="_blank">Google Maps</a>.</p>`;

//   }
// }

// function escapeHTML(str) {
//   return str.replace(/&/g, '&')
//     .replace(/</g, '<')
//     .replace(/>/g, '>')
//     .replace(/"/g, '"')
//     .replace(/'/g, '','');
// }

// function showDetails(index, name, address, specialty, phone, website) {
//   console.log("showDetails called for index:", index);
//   const detailsDiv = document.getElementById(`details-${index}`);
//   detailsDiv.style.display = 'block';
//   detailsDiv.innerHTML = `
//     <strong>${escapeHTML(name)}</strong><br>
//     Specialty: ${escapeHTML(specialty)}<br>
//     Address: ${escapeHTML(address)}<br>
//     Phone: ${escapeHTML(phone)}<br>
//     Website: ${escapeHTML(website)}
//   `;
// }

// document.addEventListener('DOMContentLoaded', () => {
//   console.log("DOM fully loaded");
//   if (document.getElementById('hospital-list')) {
//     console.log("hospital-list element found, calling initMap");
//     initMap();
//   } else {
//     console.log("hospital-list element not found");
//   }
// });


//const startSpeechRecognitionButton = document.getElementById('startSpeechRecognition');
//const transcriptionDiv = document.getElementById('transcription');
//
//startSpeechRecognitionButton.addEventListener('click', startSpeechRecognition);
//
//function startSpeechRecognition() {
//  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
//  recognition.lang = 'en-US';
//  recognition.onstart = function () {
//    startSpeechRecognitionButton.textContent = 'Listening...';
//    startSpeechRecognitionButton.disabled = true;
//  };
//  recognition.onresult = function (event) {
//    const result = event.results[0][0].transcript;
//    transcriptionDiv.textContent = result;
//  };
//  recognition.onend = function () {
//    startSpeechRecognitionButton.textContent = 'Start Speech Recognition';
//    startSpeechRecognitionButton.disabled = false;
//  };
//  recognition.start();
//}
//
//document.querySelectorAll('.modal').forEach(modal => {
//  let triggerElement = null;
//
//  modal.addEventListener('show.bs.modal', (event) => {
//    triggerElement = event.relatedTarget;
//  });
//
//  modal.addEventListener('hide.bs.modal', () => {
//    if (triggerElement) {
//      triggerElement.focus();
//    }
//  });
//
//  modal.addEventListener('hidden.bs.modal', () => {
//    if (triggerElement && document.activeElement !== triggerElement) {
//      triggerElement.focus();
//    }
//    triggerElement = null;
//  });
//});
//
//function initMap() {
//  console.log("initMap called");
//
//  let showHospitals = false;
//  let staticHospitals = [];
//  let predictedDisease = "";
//
//  // Use window.hospitalData instead of parsing data attributes
//  if (window.hospitalData) {
//    showHospitals = window.hospitalData.showHospitals || false;
//    staticHospitals = window.hospitalData.staticHospitals || [];
//    predictedDisease = window.hospitalData.predictedDisease || "";
//  } else {
//    console.error("window.hospitalData not found");
//  }
//
//  console.log("showHospitals from window.hospitalData:", showHospitals);
//  console.log("staticHospitals from window.hospitalData:", staticHospitals);
//  console.log("predictedDisease from window.hospitalData:", predictedDisease);
//
//  window.staticHospitals = Array.isArray(staticHospitals) && staticHospitals.length > 0 ? staticHospitals : [];
//  window.disease = typeof predictedDisease === 'string' && predictedDisease ? predictedDisease : "Unknown Disease";
//
//  console.log("Static Hospitals (final):", window.staticHospitals);
//  console.log("Predicted Disease (final):", window.disease);
//
//  // Enhanced searchTerm logic for more diseases
////   let searchTerm = 'hospitals near me'; // Default
////   const diseaseLower = window.disease.toLowerCase();
////   if (diseaseLower.includes('heart attack') || diseaseLower.includes('cardiac')) {
////     searchTerm = 'heart hospitals near me';
////   } else if (diseaseLower.includes('allergy')) {
////     searchTerm = 'allergy clinics near me';
////   } else if (diseaseLower.includes('diabetes')) {
////     searchTerm = 'diabetes clinics near me';
////   } else if (diseaseLower.includes('asthma')) {
////     searchTerm = 'asthma specialists near me';
////   } else if (diseaseLower.includes('cancer')) {
////     searchTerm = 'cancer treatment centers near me';
////   } else if (diseaseLower.includes('flu') || diseaseLower.includes('influenza')) {
////     searchTerm = 'urgent care near me';
////   } else if (diseaseLower.includes('tuberculosis') || diseaseLower.includes('tb')) {
////     searchTerm = 'pulmonary specialists near me';
////   } else if (diseaseLower.includes('malaria')) {
////     searchTerm = 'infectious disease specialists near me';
////   }
//
////   window.searchTerm = searchTerm;
//let searchTerm = 'hospitals';
//if (window.disease.toLowerCase().includes('heart attack')) {
//  searchTerm = 'heart hospitals';
//} else if (window.disease.toLowerCase().includes('allergy')) {
//  searchTerm = 'allergy clinics';
//} else if (window.disease.toLowerCase().includes('diabetes')) {
//  searchTerm = 'diabetes clinics';
//} else if (window.disease.toLowerCase().includes('asthma')) {
//  searchTerm = 'asthma specialists';
//}
//window.searchTerm = searchTerm;
//  console.log("Search Term:", searchTerm);
//
//  const hospitalList = document.getElementById('hospital-list');
//  if (!hospitalList) {
//    console.error("hospital-list element not found");
//    return;
//  }
//
//  console.log("Rendering static hospitals directly in initMap");
//  renderStaticHospitals(hospitalList, searchTerm);
//}
//
//function renderStaticHospitals(hospitalList, searchTerm) {
//  console.log("renderStaticHospitals called with hospitals:", window.staticHospitals);
//  hospitalList.innerHTML = ''; // Clear the "Loading..." message
//  if (window.staticHospitals.length > 0) {
//    window.staticHospitals.forEach((hospital, index) => {
//      console.log("Rendering static hospital:", hospital);
//      const facilityCard = document.createElement('div');
//      facilityCard.className = 'hospital-card';
//      facilityCard.innerHTML = `
//        <h5>${escapeHTML(hospital.name)}</h5>
//        <p><em>Specialty: ${escapeHTML(hospital.specialty)}</em></p>
//        <p>Address: ${escapeHTML(hospital.address)}</p>
//        <button class="show-details-btn" data-index="${index}" data-name="${escapeHTML(hospital.name)}" data-address="${escapeHTML(hospital.address)}" data-specialty="${escapeHTML(hospital.specialty)}" data-phone="${escapeHTML(hospital.phone)}" data-website="${escapeHTML(hospital.website)}">Show Details</button>
//        <div id="details-${index}" class="details-space"></div>
//      `;
//      hospitalList.appendChild(facilityCard);
//    });
//
//    document.querySelectorAll('.show-details-btn').forEach(button => {
//      button.addEventListener('click', () => {
//        const index = button.getAttribute('data-index');
//        const name = button.getAttribute('data-name');
//        const address = button.getAttribute('data-address');
//        const specialty = button.getAttribute('data-specialty');
//        const phone = button.getAttribute('data-phone');
//        const website = button.getAttribute('data-website');
//        showDetails(index, name, address, specialty, phone, website);
//      });
//    });
//  } else {
//    // Use window.searchTerm for the Google Maps link
//    const displayTerm = searchTerm.replace(' near me', ''); // For display purposes
//    hospitalList.innerHTML =
//      `<p>No ${displayTerm} found in static data. Please try again or search on <a href="https://www.google.com/maps/search/${encodeURIComponent(searchTerm)}" target="_blank">Google Maps</a>.</p>`;
//  }
//}
//
//function escapeHTML(str) {
//  return str.replace(/&/g, '&')
//    .replace(/</g, '<')
//    .replace(/>/g, '>')
//    .replace(/"/g, '"')
//    .replace(/'/g, '','');
//}
//
//function showDetails(index, name, address, specialty, phone, website) {
//  console.log("showDetails called for index:", index);
//  const detailsDiv = document.getElementById(`details-${index}`);
//  detailsDiv.style.display = 'block';
//  detailsDiv.innerHTML = `
//    <strong>${escapeHTML(name)}</strong><br>
//    Specialty: ${escapeHTML(specialty)}<br>
//    Address: ${escapeHTML(address)}<br>
//    Phone: ${escapeHTML(phone)}<br>
//    Website: ${escapeHTML(website)}
//  `;
//}
//
//document.addEventListener('DOMContentLoaded', () => {
//  console.log("DOM fully loaded");
//  if (document.getElementById('hospital-list')) {
//    console.log("hospital-list element found, calling initMap");
//    initMap();
//  } else {
//    console.log("hospital-list element not found");
//  }
//});

//below for maps


// const startSpeechRecognitionButton = document.getElementById('startSpeechRecognition');
// const transcriptionDiv = document.getElementById('transcription');

// startSpeechRecognitionButton.addEventListener('click', startSpeechRecognition);

// function startSpeechRecognition() {
//   const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
//   recognition.lang = 'en-US';
//   recognition.onstart = function () {
//     startSpeechRecognitionButton.textContent = 'Listening...';
//     startSpeechRecognitionButton.disabled = true;
//   };
//   recognition.onresult = function (event) {
//     const result = event.results[0][0].transcript;
//     transcriptionDiv.textContent = result;
//   };
//   recognition.onend = function () {
//     startSpeechRecognitionButton.textContent = 'Start Speech Recognition';
//     startSpeechRecognitionButton.disabled = false;
//   };
//   recognition.start();
// }

// document.querySelectorAll('.modal').forEach(modal => {
//   let triggerElement = null;

//   modal.addEventListener('show.bs.modal', (event) => {
//     triggerElement = event.relatedTarget;
//   });

//   modal.addEventListener('hide.bs.modal', () => {
//     if (triggerElement) {
//       triggerElement.focus();
//     }
//   });

//   modal.addEventListener('hidden.bs.modal', () => {
//     if (triggerElement && document.activeElement !== triggerElement) {
//       triggerElement.focus();
//     }
//     triggerElement = null;
//   });
// });

// function initMap() {
//   console.log("initMap called");

//   let showHospitals = false;
//   let staticHospitals = [];
//   let predictedDisease = "";

//   // Use window.hospitalData instead of parsing data attributes
//   if (window.hospitalData) {
//     showHospitals = window.hospitalData.showHospitals || false;
//     staticHospitals = window.hospitalData.staticHospitals || [];
//     predictedDisease = window.hospitalData.predictedDisease || "";
//   } else {
//     console.error("window.hospitalData not found");
//   }

//   console.log("showHospitals from window.hospitalData:", showHospitals);
//   console.log("staticHospitals from window.hospitalData:", staticHospitals);
//   console.log("predictedDisease from window.hospitalData:", predictedDisease);

//   window.staticHospitals = Array.isArray(staticHospitals) && staticHospitals.length > 0 ? staticHospitals : [];
//   window.disease = typeof predictedDisease === 'string' && predictedDisease ? predictedDisease : "Unknown Disease";

//   console.log("Static Hospitals (final):", window.staticHospitals);
//   console.log("Predicted Disease (final):", window.disease);

//   // Enhanced searchTerm logic for more diseases
// //   let searchTerm = 'hospitals near me'; // Default
// //   const diseaseLower = window.disease.toLowerCase();
// //   if (diseaseLower.includes('heart attack') || diseaseLower.includes('cardiac')) {
// //     searchTerm = 'heart hospitals near me';
// //   } else if (diseaseLower.includes('allergy')) {
// //     searchTerm = 'allergy clinics near me';
// //   } else if (diseaseLower.includes('diabetes')) {
// //     searchTerm = 'diabetes clinics near me';
// //   } else if (diseaseLower.includes('asthma')) {
// //     searchTerm = 'asthma specialists near me';
// //   } else if (diseaseLower.includes('cancer')) {
// //     searchTerm = 'cancer treatment centers near me';
// //   } else if (diseaseLower.includes('flu') || diseaseLower.includes('influenza')) {
// //     searchTerm = 'urgent care near me';
// //   } else if (diseaseLower.includes('tuberculosis') || diseaseLower.includes('tb')) {
// //     searchTerm = 'pulmonary specialists near me';
// //   } else if (diseaseLower.includes('malaria')) {
// //     searchTerm = 'infectious disease specialists near me';
// //   }

// //   window.searchTerm = searchTerm;
// let searchTerm = 'hospitals';
// if (window.disease.toLowerCase().includes('heart attack')) {
//   searchTerm = 'heart hospitals';
// } else if (window.disease.toLowerCase().includes('allergy')) {
//   searchTerm = 'allergy clinics';
// } else if (window.disease.toLowerCase().includes('diabetes')) {
//   searchTerm = 'diabetes clinics';
// } else if (window.disease.toLowerCase().includes('asthma')) {
//   searchTerm = 'asthma specialists';
// }
// window.searchTerm = searchTerm;
//   console.log("Search Term:", searchTerm);

//   const hospitalList = document.getElementById('hospital-list');
//   if (!hospitalList) {
//     console.error("hospital-list element not found");
//     return;
//   }

//   console.log("Rendering static hospitals directly in initMap");
//   renderStaticHospitals(hospitalList, searchTerm);
// }

// function renderStaticHospitals(hospitalList, searchTerm) {
//   console.log("renderStaticHospitals called with hospitals:", window.staticHospitals);
//   hospitalList.innerHTML = ''; // Clear the "Loading..." message
//   if (window.staticHospitals.length > 0) {
//     window.staticHospitals.forEach((hospital, index) => {
//       console.log("Rendering static hospital:", hospital);
//       const facilityCard = document.createElement('div');
//       facilityCard.className = 'hospital-card';
//       facilityCard.innerHTML = `
//         <h5>${escapeHTML(hospital.name)}</h5>
//         <p><em>Specialty: ${escapeHTML(hospital.specialty)}</em></p>
//         <p>Address: ${escapeHTML(hospital.address)}</p>
//         <button class="show-details-btn" data-index="${index}" data-name="${escapeHTML(hospital.name)}" data-address="${escapeHTML(hospital.address)}" data-specialty="${escapeHTML(hospital.specialty)}" data-phone="${escapeHTML(hospital.phone)}" data-website="${escapeHTML(hospital.website)}">Show Details</button>
//         <div id="details-${index}" class="details-space"></div>
//       `;
//       hospitalList.appendChild(facilityCard);
//     });

//     document.querySelectorAll('.show-details-btn').forEach(button => {
//       button.addEventListener('click', () => {
//         const index = button.getAttribute('data-index');
//         const name = button.getAttribute('data-name');
//         const address = button.getAttribute('data-address');
//         const specialty = button.getAttribute('data-specialty');
//         const phone = button.getAttribute('data-phone');
//         const website = button.getAttribute('data-website');
//         showDetails(index, name, address, specialty, phone, website);
//       });
//     });
//   } else {
//     // Use window.searchTerm for the Google Maps link
//     const displayTerm = searchTerm.replace(' near me', ''); // For display purposes
//     hospitalList.innerHTML =
//     //   `<p>No ${displayTerm} found in static data. Please try again or search on <a href="https://www.google.com/maps/search/${encodeURIComponent(searchTerm)}" target="_blank">Google Maps</a>.</p>`;
//           `<p>For Nearby hospitals <a href="https://www.google.com/maps/search/${encodeURIComponent(searchTerm)}" target="_blank">Click here</a>.</p>`;

//   }
// }

// function escapeHTML(str) {
//   return str.replace(/&/g, '&')
//     .replace(/</g, '<')
//     .replace(/>/g, '>')
//     .replace(/"/g, '"')
//     .replace(/'/g, '','');
// }

// function showDetails(index, name, address, specialty, phone, website) {
//   console.log("showDetails called for index:", index);
//   const detailsDiv = document.getElementById(`details-${index}`);
//   detailsDiv.style.display = 'block';
//   detailsDiv.innerHTML = `
//     <strong>${escapeHTML(name)}</strong><br>
//     Specialty: ${escapeHTML(specialty)}<br>
//     Address: ${escapeHTML(address)}<br>
//     Phone: ${escapeHTML(phone)}<br>
//     Website: ${escapeHTML(website)}
//   `;
// }

// document.addEventListener('DOMContentLoaded', () => {
//   console.log("DOM fully loaded");
//   if (document.getElementById('hospital-list')) {
//     console.log("hospital-list element found, calling initMap");
//     initMap();
//   } else {
//     console.log("hospital-list element not found");
//   }
// });
// chat below 


const startSpeechRecognitionButton = document.getElementById('startSpeechRecognition');
const transcriptionDiv = document.getElementById('transcription');
const startChatbotButton = document.getElementById('startChatbot');
const chatbotIcon = document.getElementById('chatbot-icon');
const chatbotContainer = document.getElementById('chatbot-container');
const chatbotClose = document.getElementById('chatbot-close');
const chatbotBody = document.getElementById('chatbot-body');
const chatbotInput = document.getElementById('chatbot-input');
const chatbotSend = document.getElementById('chatbot-send');
const symptomInput = document.getElementById('symptoms');
const symptomForm = document.getElementById('symptom-form');

// Chatbot state
let chatbotState = {
  step: 'initial',
  symptoms: [],
  primarySymptom: null,
  followUpQuestions: {
    'chest_pain': [
      { question: 'Does your chest pain worsen with movement?', symptomIfYes: 'movement_stiffness', symptomIfNo: null },
      { question: 'Are you experiencing breathlessness along with chest pain?', symptomIfYes: 'breathlessness', symptomIfNo: null },
      { question: 'Do you have a fast heart rate?', symptomIfYes: 'fast_heart_rate', symptomIfNo: null }
    ],
    'continuous_sneezing': [
      { question: 'Do you have itching along with sneezing?', symptomIfYes: 'itching', symptomIfNo: null },
      { question: 'Are you experiencing a runny nose?', symptomIfYes: 'runny_nose', symptomIfNo: null },
      { question: 'Do you have a sore throat?', symptomIfYes: 'throat_irritation', symptomIfNo: null }
    ],
    'fever': [
      { question: 'Is your fever high (above 100.4°F)?', symptomIfYes: 'high_fever', symptomIfNo: 'mild_fever' },
      { question: 'Are you experiencing chills?', symptomIfYes: 'chills', symptomIfNo: null },
      { question: 'Do you have a cough?', symptomIfYes: 'cough', symptomIfNo: null }
    ],
    'headache': [
      { question: 'Do you feel dizzy along with your headache?', symptomIfYes: 'dizziness', symptomIfNo: null },
      { question: 'Are you experiencing nausea?', symptomIfYes: 'nausea', symptomIfNo: null },
      { question: 'Do you have a stiff neck?', symptomIfYes: 'stiff_neck', symptomIfNo: null }
    ],
    'fatigue': [
      { question: 'Are you feeling lethargic?', symptomIfYes: 'lethargy', symptomIfNo: null },
      { question: 'Do you have muscle weakness?', symptomIfYes: 'muscle_weakness', symptomIfNo: null },
      { question: 'Are you experiencing weight loss?', symptomIfYes: 'weight_loss', symptomIfNo: null }
    ],
    'cough': [
      { question: 'Is your cough accompanied by phlegm?', symptomIfYes: 'phlegm', symptomIfNo: null },
      { question: 'Do you have a fever?', symptomIfYes: 'fever', symptomIfNo: null },
      { question: 'Are you experiencing throat irritation?', symptomIfYes: 'throat_irritation', symptomIfNo: null }
    ],
    'vomiting': [
      { question: 'Are you experiencing nausea?', symptomIfYes: 'nausea', symptomIfNo: null },
      { question: 'Do you have abdominal pain?', symptomIfYes: 'abdominal_pain', symptomIfNo: null },
      { question: 'Are you dehydrated?', symptomIfYes: 'dehydration', symptomIfNo: null }
    ]
  },
  currentQuestionIndex: 0
};

// Initialize chatbot
function initChatbot() {
  if (!window.symptoms_dict) {
    console.error('window.symptoms_dict is not defined. Ensure it is passed from the server.');
    return;
  }

  // Open chatbot when clicking the "Chat with Symptom Assistant" button or the icon
  startChatbotButton.addEventListener('click', openChatbot);
  chatbotIcon.addEventListener('click', openChatbot);
  chatbotClose.addEventListener('click', closeChatbot);

  // Handle sending messages
  chatbotSend.addEventListener('click', handleChatbotInput);
  chatbotInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
      handleChatbotInput();
    }
  });
}

function openChatbot() {
  chatbotContainer.style.display = 'flex';
  chatbotIcon.style.display = 'none';
  chatbotInput.focus();
}

function closeChatbot() {
  chatbotContainer.style.display = 'none';
  chatbotIcon.style.display = 'flex';
  resetChatbot();
}

function resetChatbot() {
  chatbotState = {
    step: 'initial',
    symptoms: [],
    primarySymptom: null,
    followUpQuestions: chatbotState.followUpQuestions,
    currentQuestionIndex: 0
  };
  chatbotBody.innerHTML = '<div class="chat-message bot">Hello! I\'m here to help you describe your symptoms. What is your main symptom right now?</div>';
  symptomInput.value = '';
}

function addChatMessage(message, sender) {
  const messageDiv = document.createElement('div');
  messageDiv.className = `chat-message ${sender}`;
  messageDiv.textContent = message;
  chatbotBody.appendChild(messageDiv);
  chatbotBody.scrollTop = chatbotBody.scrollHeight;
}

function handleChatbotInput() {
  const userInput = chatbotInput.value.trim().toLowerCase();
  if (!userInput) return;

  addChatMessage(userInput, 'user');
  chatbotInput.value = '';

  console.log('Current Step:', chatbotState.step, 'User Input:', userInput); // Debug log

  switch (chatbotState.step) {
    case 'initial':
      handleInitialSymptom(userInput);
      break;
    case 'follow-up':
      handleFollowUpResponse(userInput);
      break;
    case 'more-symptoms':
      handleMoreSymptoms(userInput);
      break;
    case 'done':
      addChatMessage('I’ve already collected your symptoms. Please click "Get Recommendations" to see your results, or close this chat to start over.', 'bot');
      break;
  }
}

function handleInitialSymptom(userInput) {
  const symptom = Object.keys(window.symptoms_dict).find(s => userInput.includes(s.replace('_', ' ')));
  if (symptom) {
    chatbotState.primarySymptom = symptom;
    chatbotState.symptoms.push(symptom);
    symptomInput.value = chatbotState.symptoms.join(', ');
    console.log('Recognized Symptom:', symptom, 'Updated Symptoms:', chatbotState.symptoms); // Debug log

    if (chatbotState.followUpQuestions[symptom]) {
      chatbotState.step = 'follow-up';
      chatbotState.currentQuestionIndex = 0;
      const question = chatbotState.followUpQuestions[symptom][0].question;
      addChatMessage(question, 'bot');
    } else {
      chatbotState.step = 'more-symptoms';
      addChatMessage(`I’ve noted ${symptom.replace('_', ' ')}. I don’t have specific follow-up questions for this symptom. Do you have any other symptoms? (Type "no" if you’re done)`, 'bot');
    }
  } else {
    addChatMessage('I didn’t recognize that symptom. Please try again (e.g., chest pain, fever, headache). You can also type symptoms as they appear in the placeholder, like "chest_pain".', 'bot');
  }
}

function handleFollowUpResponse(userInput) {
  const currentQuestion = chatbotState.followUpQuestions[chatbotState.primarySymptom][chatbotState.currentQuestionIndex];
  const isYes = userInput.includes('yes') || userInput.includes('y') || userInput.includes('yeah') || userInput.includes('yep');
  const isNo = userInput.includes('no') || userInput.includes('n') || userInput.includes('nope') || userInput.includes('nah');

  console.log('Follow-up Response:', userInput, 'Is Yes:', isYes, 'Is No:', isNo); // Debug log

  if (!isYes && !isNo) {
    addChatMessage('Please answer with "yes" or "no" (e.g., yes, y, no, n).', 'bot');
    return;
  }

  if (isYes && currentQuestion.symptomIfYes) {
    chatbotState.symptoms.push(currentQuestion.symptomIfYes);
    symptomInput.value = chatbotState.symptoms.join(', ');
    console.log('Added Symptom (Yes):', currentQuestion.symptomIfYes, 'Updated Symptoms:', chatbotState.symptoms); // Debug log
  } else if (isNo && currentQuestion.symptomIfNo) {
    chatbotState.symptoms.push(currentQuestion.symptomIfNo);
    symptomInput.value = chatbotState.symptoms.join(', ');
    console.log('Added Symptom (No):', currentQuestion.symptomIfNo, 'Updated Symptoms:', chatbotState.symptoms); // Debug log
  }

  chatbotState.currentQuestionIndex++;
  if (chatbotState.currentQuestionIndex < chatbotState.followUpQuestions[chatbotState.primarySymptom].length) {
    const nextQuestion = chatbotState.followUpQuestions[chatbotState.primarySymptom][chatbotState.currentQuestionIndex].question;
    addChatMessage(nextQuestion, 'bot');
  } else {
    chatbotState.step = 'more-symptoms';
    addChatMessage('Thanks for answering! Do you have any other symptoms? (Type "no" if you’re done)', 'bot');
  }
}

function handleMoreSymptoms(userInput) {
  if (userInput.includes('no') || userInput.includes('n') || userInput.includes('nope') || userInput.includes('nah')) {
    chatbotState.step = 'done';
    addChatMessage(`I’ve updated the symptom input field with: ${chatbotState.symptoms.join(', ')}. I’ll now submit the form to get your recommendations. Please wait...`, 'bot');
    console.log('Final Symptoms:', chatbotState.symptoms); // Debug log
    // Submit the form programmatically
    setTimeout(() => {
      symptomForm.submit();
    }, 1000); // Delay to allow user to read the message
  } else {
    const symptom = Object.keys(window.symptoms_dict).find(s => userInput.includes(s.replace('_', ' ')));
    if (symptom) {
      chatbotState.symptoms.push(symptom);
      symptomInput.value = chatbotState.symptoms.join(', ');
      console.log('Added Additional Symptom:', symptom, 'Updated Symptoms:', chatbotState.symptoms); // Debug log
      addChatMessage(`Added ${symptom.replace('_', ' ')}. Any more symptoms? (Type "no" if you’re done)`, 'bot');
    } else {
      addChatMessage('I didn’t recognize that symptom. Please try again or type "no" to finish.', 'bot');
    }
  }
}

// Speech Recognition
startSpeechRecognitionButton.addEventListener('click', startSpeechRecognition);

function startSpeechRecognition() {
  const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  recognition.lang = 'en-US';
  recognition.onstart = function () {
    startSpeechRecognitionButton.textContent = 'Listening...';
    startSpeechRecognitionButton.disabled = true;
  };
  recognition.onresult = function (event) {
    const result = event.results[0][0].transcript;
    transcriptionDiv.textContent = result;
  };
  recognition.onend = function () {
    startSpeechRecognitionButton.textContent = 'Start Speech Recognition';
    startSpeechRecognitionButton.disabled = false;
  };
  recognition.start();
}

// Modal Accessibility
document.querySelectorAll('.modal').forEach(modal => {
  let triggerElement = null;

  modal.addEventListener('show.bs.modal', (event) => {
    triggerElement = event.relatedTarget;
  });

  modal.addEventListener('hide.bs.modal', () => {
    if (triggerElement) {
      triggerElement.focus();
    }
  });

  modal.addEventListener('hidden.bs.modal', () => {
    if (triggerElement && document.activeElement !== triggerElement) {
      triggerElement.focus();
    }
    triggerElement = null;
  });
});

// Hospital Rendering
function initMap() {
  console.log("initMap called");

  let showHospitals = false;
  let staticHospitals = [];
  let predictedDisease = "";

  if (window.hospitalData) {
    showHospitals = window.hospitalData.showHospitals || false;
    staticHospitals = window.hospitalData.staticHospitals || [];
    predictedDisease = window.hospitalData.predictedDisease || "";
  } else {
    console.error("window.hospitalData not found");
  }

  console.log("showHospitals from window.hospitalData:", showHospitals);
  console.log("staticHospitals from window.hospitalData:", staticHospitals);
  console.log("predictedDisease from window.hospitalData:", predictedDisease);

  window.staticHospitals = Array.isArray(staticHospitals) && staticHospitals.length > 0 ? staticHospitals : [];
  window.disease = typeof predictedDisease === 'string' && predictedDisease ? predictedDisease : "Unknown Disease";

  console.log("Static Hospitals (final):", window.staticHospitals);
  console.log("Predicted Disease (final):", window.disease);

  let searchTerm = 'hospitals';
  if (window.disease.toLowerCase().includes('heart attack')) {
    searchTerm = 'heart hospitals';
  } else if (window.disease.toLowerCase().includes('allergy')) {
    searchTerm = 'allergy clinics';
  } else if (window.disease.toLowerCase().includes('diabetes')) {
    searchTerm = 'diabetes clinics';
  } else if (window.disease.toLowerCase().includes('asthma')) {
    searchTerm = 'asthma specialists';
  }
  window.searchTerm = searchTerm;
  console.log("Search Term:", searchTerm);

  const hospitalList = document.getElementById('hospital-list');
  if (!hospitalList) {
    console.error("hospital-list element not found");
    return;
  }

  console.log("Rendering static hospitals directly in initMap");
  renderStaticHospitals(hospitalList, searchTerm);
}

function renderStaticHospitals(hospitalList, searchTerm) {
  console.log("renderStaticHospitals called with hospitals:", window.staticHospitals);
  hospitalList.innerHTML = '';
  if (window.staticHospitals.length > 0) {
    window.staticHospitals.forEach((hospital, index) => {
      console.log("Rendering static hospital:", hospital);
      const facilityCard = document.createElement('div');
      facilityCard.className = 'hospital-card';
      facilityCard.innerHTML = `
        <h5>${escapeHTML(hospital.name)}</h5>
        <p><em>Specialty: ${escapeHTML(hospital.specialty)}</em></p>
        <p>Address: ${escapeHTML(hospital.address)}</p>
        <button class="show-details-btn" data-index="${index}" data-name="${escapeHTML(hospital.name)}" data-address="${escapeHTML(hospital.address)}" data-specialty="${escapeHTML(hospital.specialty)}" data-phone="${escapeHTML(hospital.phone)}" data-website="${escapeHTML(hospital.website)}">Show Details</button>
        <div id="details-${index}" class="details-space"></div>
      `;
      hospitalList.appendChild(facilityCard);
    });

    document.querySelectorAll('.show-details-btn').forEach(button => {
      button.addEventListener('click', () => {
        const index = button.getAttribute('data-index');
        const name = button.getAttribute('data-name');
        const address = button.getAttribute('data-address');
        const specialty = button.getAttribute('data-specialty');
        const phone = button.getAttribute('data-phone');
        const website = button.getAttribute('data-website');
        showDetails(index, name, address, specialty, phone, website);
      });
    });
  } else {
    hospitalList.innerHTML = `<p>For Nearby hospitals <a href="https://www.google.com/maps/search/${encodeURIComponent(searchTerm)}" target="_blank">Click here</a>.</p>`;
  }
}

function escapeHTML(str) {
  return str.replace(/&/g, '&')
    .replace(/</g, '<')
    .replace(/>/g, '>')
    .replace(/"/g, '"')
    .replace(/'/g, '','');
}

function showDetails(index, name, address, specialty, phone, website) {
  console.log("showDetails called for index:", index);
  const detailsDiv = document.getElementById(`details-${index}`);
  detailsDiv.style.display = 'block';
  detailsDiv.innerHTML = `
    <strong>${escapeHTML(name)}</strong><br>
    Specialty: ${escapeHTML(specialty)}<br>
    Address: ${escapeHTML(address)}<br>
    Phone: ${escapeHTML(phone)}<br>
    Website: ${escapeHTML(website)}
  `;
}

document.addEventListener('DOMContentLoaded', () => {
  console.log("DOM fully loaded");
  initChatbot();
  if (document.getElementById('hospital-list')) {
    console.log("hospital-list element found, calling initMap");
    initMap();
  } else {
    console.log("hospital-list element not found");
  }
});