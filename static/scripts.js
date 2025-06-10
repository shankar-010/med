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


// const startSpeechRecognitionButton = document.getElementById('startSpeechRecognition');
// const transcriptionDiv = document.getElementById('transcription');
// const startChatbotButton = document.getElementById('startChatbot');
// const chatbotIcon = document.getElementById('chatbot-icon');
// const chatbotContainer = document.getElementById('chatbot-container');
// const chatbotClose = document.getElementById('chatbot-close');
// const chatbotBody = document.getElementById('chatbot-body');
// const chatbotInput = document.getElementById('chatbot-input');
// const chatbotSend = document.getElementById('chatbot-send');
// const symptomInput = document.getElementById('symptoms');
// const symptomForm = document.getElementById('symptom-form');

// // Chatbot state
// let chatbotState = {
//   step: 'initial',
//   symptoms: [],
//   primarySymptom: null,
//   followUpQuestions: {
//     'chest_pain': [
//       { question: 'Does your chest pain worsen with movement?', symptomIfYes: 'movement_stiffness', symptomIfNo: null },
//       { question: 'Are you experiencing breathlessness along with chest pain?', symptomIfYes: 'breathlessness', symptomIfNo: null },
//       { question: 'Do you have a fast heart rate?', symptomIfYes: 'fast_heart_rate', symptomIfNo: null }
//     ],
//     'continuous_sneezing': [
//       { question: 'Do you have itching along with sneezing?', symptomIfYes: 'itching', symptomIfNo: null },
//       { question: 'Are you experiencing a runny nose?', symptomIfYes: 'runny_nose', symptomIfNo: null },
//       { question: 'Do you have a sore throat?', symptomIfYes: 'throat_irritation', symptomIfNo: null }
//     ],
//     'fever': [
//       { question: 'Is your fever high (above 100.4°F)?', symptomIfYes: 'high_fever', symptomIfNo: 'mild_fever' },
//       { question: 'Are you experiencing chills?', symptomIfYes: 'chills', symptomIfNo: null },
//       { question: 'Do you have a cough?', symptomIfYes: 'cough', symptomIfNo: null }
//     ],
//     'headache': [
//       { question: 'Do you feel dizzy along with your headache?', symptomIfYes: 'dizziness', symptomIfNo: null },
//       { question: 'Are you experiencing nausea?', symptomIfYes: 'nausea', symptomIfNo: null },
//       { question: 'Do you have a stiff neck?', symptomIfYes: 'stiff_neck', symptomIfNo: null }
//     ],
//     'fatigue': [
//       { question: 'Are you feeling lethargic?', symptomIfYes: 'lethargy', symptomIfNo: null },
//       { question: 'Do you have muscle weakness?', symptomIfYes: 'muscle_weakness', symptomIfNo: null },
//       { question: 'Are you experiencing weight loss?', symptomIfYes: 'weight_loss', symptomIfNo: null }
//     ],
//     'cough': [
//       { question: 'Is your cough accompanied by phlegm?', symptomIfYes: 'phlegm', symptomIfNo: null },
//       { question: 'Do you have a fever?', symptomIfYes: 'fever', symptomIfNo: null },
//       { question: 'Are you experiencing throat irritation?', symptomIfYes: 'throat_irritation', symptomIfNo: null }
//     ],
//     'vomiting': [
//       { question: 'Are you experiencing nausea?', symptomIfYes: 'nausea', symptomIfNo: null },
//       { question: 'Do you have abdominal pain?', symptomIfYes: 'abdominal_pain', symptomIfNo: null },
//       { question: 'Are you dehydrated?', symptomIfYes: 'dehydration', symptomIfNo: null }
//     ]
//   },
//   currentQuestionIndex: 0
// };

// // Initialize chatbot
// function initChatbot() {
//   if (!window.symptoms_dict) {
//     console.error('window.symptoms_dict is not defined. Ensure it is passed from the server.');
//     return;
//   }

//   // Open chatbot when clicking the "Chat with Symptom Assistant" button or the icon
//   startChatbotButton.addEventListener('click', openChatbot);
//   chatbotIcon.addEventListener('click', openChatbot);
//   chatbotClose.addEventListener('click', closeChatbot);

//   // Handle sending messages
//   chatbotSend.addEventListener('click', handleChatbotInput);
//   chatbotInput.addEventListener('keypress', (e) => {
//     if (e.key === 'Enter') {
//       handleChatbotInput();
//     }
//   });
// }

// function openChatbot() {
//   chatbotContainer.style.display = 'flex';
//   chatbotIcon.style.display = 'none';
//   chatbotInput.focus();
// }

// function closeChatbot() {
//   chatbotContainer.style.display = 'none';
//   chatbotIcon.style.display = 'flex';
//   resetChatbot();
// }

// function resetChatbot() {
//   chatbotState = {
//     step: 'initial',
//     symptoms: [],
//     primarySymptom: null,
//     followUpQuestions: chatbotState.followUpQuestions,
//     currentQuestionIndex: 0
//   };
//   chatbotBody.innerHTML = '<div class="chat-message bot">Hello! I\'m here to help you describe your symptoms. What is your main symptom right now?</div>';
//   symptomInput.value = '';
// }

// function addChatMessage(message, sender) {
//   const messageDiv = document.createElement('div');
//   messageDiv.className = `chat-message ${sender}`;
//   messageDiv.textContent = message;
//   chatbotBody.appendChild(messageDiv);
//   chatbotBody.scrollTop = chatbotBody.scrollHeight;
// }

// function handleChatbotInput() {
//   const userInput = chatbotInput.value.trim().toLowerCase();
//   if (!userInput) return;

//   addChatMessage(userInput, 'user');
//   chatbotInput.value = '';

//   console.log('Current Step:', chatbotState.step, 'User Input:', userInput); // Debug log

//   switch (chatbotState.step) {
//     case 'initial':
//       handleInitialSymptom(userInput);
//       break;
//     case 'follow-up':
//       handleFollowUpResponse(userInput);
//       break;
//     case 'more-symptoms':
//       handleMoreSymptoms(userInput);
//       break;
//     case 'done':
//       addChatMessage('I’ve already collected your symptoms. Please click "Get Recommendations" to see your results, or close this chat to start over.', 'bot');
//       break;
//   }
// }

// function handleInitialSymptom(userInput) {
//   const symptom = Object.keys(window.symptoms_dict).find(s => userInput.includes(s.replace('_', ' ')));
//   if (symptom) {
//     chatbotState.primarySymptom = symptom;
//     chatbotState.symptoms.push(symptom);
//     symptomInput.value = chatbotState.symptoms.join(', ');
//     console.log('Recognized Symptom:', symptom, 'Updated Symptoms:', chatbotState.symptoms); // Debug log

//     if (chatbotState.followUpQuestions[symptom]) {
//       chatbotState.step = 'follow-up';
//       chatbotState.currentQuestionIndex = 0;
//       const question = chatbotState.followUpQuestions[symptom][0].question;
//       addChatMessage(question, 'bot');
//     } else {
//       chatbotState.step = 'more-symptoms';
//       addChatMessage(`I’ve noted ${symptom.replace('_', ' ')}. I don’t have specific follow-up questions for this symptom. Do you have any other symptoms? (Type "no" if you’re done)`, 'bot');
//     }
//   } else {
//     addChatMessage('I didn’t recognize that symptom. Please try again (e.g., chest pain, fever, headache). You can also type symptoms as they appear in the placeholder, like "chest_pain".', 'bot');
//   }
// }

// function handleFollowUpResponse(userInput) {
//   const currentQuestion = chatbotState.followUpQuestions[chatbotState.primarySymptom][chatbotState.currentQuestionIndex];
//   const isYes = userInput.includes('yes') || userInput.includes('y') || userInput.includes('yeah') || userInput.includes('yep');
//   const isNo = userInput.includes('no') || userInput.includes('n') || userInput.includes('nope') || userInput.includes('nah');

//   console.log('Follow-up Response:', userInput, 'Is Yes:', isYes, 'Is No:', isNo); // Debug log

//   if (!isYes && !isNo) {
//     addChatMessage('Please answer with "yes" or "no" (e.g., yes, y, no, n).', 'bot');
//     return;
//   }

//   if (isYes && currentQuestion.symptomIfYes) {
//     chatbotState.symptoms.push(currentQuestion.symptomIfYes);
//     symptomInput.value = chatbotState.symptoms.join(', ');
//     console.log('Added Symptom (Yes):', currentQuestion.symptomIfYes, 'Updated Symptoms:', chatbotState.symptoms); // Debug log
//   } else if (isNo && currentQuestion.symptomIfNo) {
//     chatbotState.symptoms.push(currentQuestion.symptomIfNo);
//     symptomInput.value = chatbotState.symptoms.join(', ');
//     console.log('Added Symptom (No):', currentQuestion.symptomIfNo, 'Updated Symptoms:', chatbotState.symptoms); // Debug log
//   }

//   chatbotState.currentQuestionIndex++;
//   if (chatbotState.currentQuestionIndex < chatbotState.followUpQuestions[chatbotState.primarySymptom].length) {
//     const nextQuestion = chatbotState.followUpQuestions[chatbotState.primarySymptom][chatbotState.currentQuestionIndex].question;
//     addChatMessage(nextQuestion, 'bot');
//   } else {
//     chatbotState.step = 'more-symptoms';
//     addChatMessage('Thanks for answering! Do you have any other symptoms? (Type "no" if you’re done)', 'bot');
//   }
// }

// function handleMoreSymptoms(userInput) {
//   if (userInput.includes('no') || userInput.includes('n') || userInput.includes('nope') || userInput.includes('nah')) {
//     chatbotState.step = 'done';
//     addChatMessage(`I’ve updated the symptom input field with: ${chatbotState.symptoms.join(', ')}. I’ll now submit the form to get your recommendations. Please wait...`, 'bot');
//     console.log('Final Symptoms:', chatbotState.symptoms); // Debug log
//     // Submit the form programmatically
//     setTimeout(() => {
//       symptomForm.submit();
//     }, 1000); // Delay to allow user to read the message
//   } else {
//     const symptom = Object.keys(window.symptoms_dict).find(s => userInput.includes(s.replace('_', ' ')));
//     if (symptom) {
//       chatbotState.symptoms.push(symptom);
//       symptomInput.value = chatbotState.symptoms.join(', ');
//       console.log('Added Additional Symptom:', symptom, 'Updated Symptoms:', chatbotState.symptoms); // Debug log
//       addChatMessage(`Added ${symptom.replace('_', ' ')}. Any more symptoms? (Type "no" if you’re done)`, 'bot');
//     } else {
//       addChatMessage('I didn’t recognize that symptom. Please try again or type "no" to finish.', 'bot');
//     }
//   }
// }

// // Speech Recognition
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

// // Modal Accessibility
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

// // Hospital Rendering
// function initMap() {
//   console.log("initMap called");

//   let showHospitals = false;
//   let staticHospitals = [];
//   let predictedDisease = "";

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

//   let searchTerm = 'hospitals';
//   if (window.disease.toLowerCase().includes('heart attack')) {
//     searchTerm = 'heart hospitals';
//   } else if (window.disease.toLowerCase().includes('allergy')) {
//     searchTerm = 'allergy clinics';
//   } else if (window.disease.toLowerCase().includes('diabetes')) {
//     searchTerm = 'diabetes clinics';
//   } else if (window.disease.toLowerCase().includes('asthma')) {
//     searchTerm = 'asthma specialists';
//   }
//   window.searchTerm = searchTerm;
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
//   hospitalList.innerHTML = '';
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
//     hospitalList.innerHTML = `<p>For Nearby hospitals <a href="https://www.google.com/maps/search/${encodeURIComponent(searchTerm)}" target="_blank">Click here</a>.</p>`;
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
//   initChatbot();
//   if (document.getElementById('hospital-list')) {
//     console.log("hospital-list element found, calling initMap");
//     initMap();
//   } else {
//     console.log("hospital-list element not found");
//   }
// });
// lab below




// const startSpeechRecognitionButton = document.getElementById('startSpeechRecognition');
// const transcriptionDiv = document.getElementById('transcription');
// const startChatbotButton = document.getElementById('startChatbot');
// const chatbotIcon = document.getElementById('chatbot-icon');
// const chatbotContainer = document.getElementById('chatbot-container');
// const chatbotClose = document.getElementById('chatbot-close');
// const chatbotBody = document.getElementById('chatbot-body');
// const chatbotInput = document.getElementById('chatbot-input');
// const chatbotSend = document.getElementById('chatbot-send');
// const symptomInput = document.getElementById('symptoms');
// const symptomForm = document.getElementById('symptom-form');
// const labTestForm = document.getElementById('lab-test-form');

// // Chatbot state
// let chatbotState = {
//   step: 'initial',
//   symptoms: [],
//   primarySymptom: null,
//   followUpQuestions: {
//     'chest_pain': [
//       { question: 'Does your chest pain worsen with movement?', symptomIfYes: 'movement_stiffness', symptomIfNo: null },
//       { question: 'Are you experiencing breathlessness along with chest pain?', symptomIfYes: 'breathlessness', symptomIfNo: null },
//       { question: 'Do you have a fast heart rate?', symptomIfYes: 'fast_heart_rate', symptomIfNo: null }
//     ],
//     'continuous_sneezing': [
//       { question: 'Do you have itching along with sneezing?', symptomIfYes: 'itching', symptomIfNo: null },
//       { question: 'Are you experiencing a runny nose?', symptomIfYes: 'runny_nose', symptomIfNo: null },
//       { question: 'Do you have a sore throat?', symptomIfYes: 'throat_irritation', symptomIfNo: null }
//     ],
//     'fever': [
//       { question: 'Is your fever high (above 100.4°F)?', symptomIfYes: 'high_fever', symptomIfNo: 'mild_fever' },
//       { question: 'Are you experiencing chills?', symptomIfYes: 'chills', symptomIfNo: null },
//       { question: 'Do you have a cough?', symptomIfYes: 'cough', symptomIfNo: null }
//     ],
//     'headache': [
//       { question: 'Do you feel dizzy along with your headache?', symptomIfYes: 'dizziness', symptomIfNo: null },
//       { question: 'Are you experiencing nausea?', symptomIfYes: 'nausea', symptomIfNo: null },
//       { question: 'Do you have a stiff neck?', symptomIfYes: 'stiff_neck', symptomIfNo: null }
//     ],
//     'fatigue': [
//       { question: 'Are you feeling lethargic?', symptomIfYes: 'lethargy', symptomIfNo: null },
//       { question: 'Do you have muscle weakness?', symptomIfYes: 'muscle_weakness', symptomIfNo: null },
//       { question: 'Are you experiencing weight loss?', symptomIfYes: 'weight_loss', symptomIfNo: null }
//     ],
//     'cough': [
//       { question: 'Is your cough accompanied by phlegm?', symptomIfYes: 'phlegm', symptomIfNo: null },
//       { question: 'Do you have a fever?', symptomIfYes: 'fever', symptomIfNo: null },
//       { question: 'Are you experiencing throat irritation?', symptomIfYes: 'throat_irritation', symptomIfNo: null }
//     ],
//     'vomiting': [
//       { question: 'Are you experiencing nausea?', symptomIfYes: 'nausea', symptomIfNo: null },
//       { question: 'Do you have abdominal pain?', symptomIfYes: 'abdominal_pain', symptomIfNo: null },
//       { question: 'Are you dehydrated?', symptomIfYes: 'dehydration', symptomIfNo: null }
//     ]
//   },
//   currentQuestionIndex: 0
// };

// // Initialize chatbot
// function initChatbot() {
//   if (!window.symptoms_dict) {
//     console.error('window.symptoms_dict is not defined. Ensure it is passed from the server.');
//     return;
//   }

//   // Open chatbot when clicking the "Chat with Symptom Assistant" button or the icon
//   startChatbotButton.addEventListener('click', openChatbot);
//   chatbotIcon.addEventListener('click', openChatbot);
//   chatbotClose.addEventListener('click', closeChatbot);

//   // Handle sending messages
//   chatbotSend.addEventListener('click', handleChatbotInput);
//   chatbotInput.addEventListener('keypress', (e) => {
//     if (e.key === 'Enter') {
//       handleChatbotInput();
//     }
//   });
// }

// function openChatbot() {
//   chatbotContainer.style.display = 'flex';
//   chatbotIcon.style.display = 'none';
//   chatbotInput.focus();
// }

// function closeChatbot() {
//   chatbotContainer.style.display = 'none';
//   chatbotIcon.style.display = 'flex';
//   resetChatbot();
// }

// function resetChatbot() {
//   chatbotState = {
//     step: 'initial',
//     symptoms: [],
//     primarySymptom: null,
//     followUpQuestions: chatbotState.followUpQuestions,
//     currentQuestionIndex: 0
//   };
//   chatbotBody.innerHTML = '<div class="chat-message bot">Hello! I\'m here to help you describe your symptoms. What is your main symptom right now?</div>';
//   symptomInput.value = '';
// }

// function addChatMessage(message, sender) {
//   const messageDiv = document.createElement('div');
//   messageDiv.className = `chat-message ${sender}`;
//   messageDiv.textContent = message;
//   chatbotBody.appendChild(messageDiv);
//   chatbotBody.scrollTop = chatbotBody.scrollHeight;
// }

// function handleChatbotInput() {
//   const userInput = chatbotInput.value.trim().toLowerCase();
//   if (!userInput) return;

//   addChatMessage(userInput, 'user');
//   chatbotInput.value = '';

//   console.log('Current Step:', chatbotState.step, 'User Input:', userInput); // Debug log

//   switch (chatbotState.step) {
//     case 'initial':
//       handleInitialSymptom(userInput);
//       break;
//     case 'follow-up':
//       handleFollowUpResponse(userInput);
//       break;
//     case 'more-symptoms':
//       handleMoreSymptoms(userInput);
//       break;
//     case 'done':
//       addChatMessage('I’ve already collected your symptoms. Please click "Get Recommendations" to see your results, or close this chat to start over.', 'bot');
//       break;
//   }
// }

// function handleInitialSymptom(userInput) {
//   const symptom = Object.keys(window.symptoms_dict).find(s => userInput.includes(s.replace('_', ' ')));
//   if (symptom) {
//     chatbotState.primarySymptom = symptom;
//     chatbotState.symptoms.push(symptom);
//     symptomInput.value = chatbotState.symptoms.join(', ');
//     console.log('Recognized Symptom:', symptom, 'Updated Symptoms:', chatbotState.symptoms); // Debug log

//     if (chatbotState.followUpQuestions[symptom]) {
//       chatbotState.step = 'follow-up';
//       chatbotState.currentQuestionIndex = 0;
//       const question = chatbotState.followUpQuestions[symptom][0].question;
//       addChatMessage(question, 'bot');
//     } else {
//       chatbotState.step = 'more-symptoms';
//       addChatMessage(`I’ve noted ${symptom.replace('_', ' ')}. I don’t have specific follow-up questions for this symptom. Do you have any other symptoms? (Type "no" if you’re done)`, 'bot');
//     }
//   } else {
//     addChatMessage('I didn’t recognize that symptom. Please try again (e.g., chest pain, fever, headache). You can also type symptoms as they appear in the placeholder, like "chest_pain".', 'bot');
//   }
// }

// function handleFollowUpResponse(userInput) {
//   const currentQuestion = chatbotState.followUpQuestions[chatbotState.primarySymptom][chatbotState.currentQuestionIndex];
//   const isYes = userInput.includes('yes') || userInput.includes('y') || userInput.includes('yeah') || userInput.includes('yep');
//   const isNo = userInput.includes('no') || userInput.includes('n') || userInput.includes('nope') || userInput.includes('nah');

//   console.log('Follow-up Response:', userInput, 'Is Yes:', isYes, 'Is No:', isNo); // Debug log

//   if (!isYes && !isNo) {
//     addChatMessage('Please answer with "yes" or "no" (e.g., yes, y, no, n).', 'bot');
//     return;
//   }

//   if (isYes && currentQuestion.symptomIfYes) {
//     chatbotState.symptoms.push(currentQuestion.symptomIfYes);
//     symptomInput.value = chatbotState.symptoms.join(', ');
//     console.log('Added Symptom (Yes):', currentQuestion.symptomIfYes, 'Updated Symptoms:', chatbotState.symptoms); // Debug log
//   } else if (isNo && currentQuestion.symptomIfNo) {
//     chatbotState.symptoms.push(currentQuestion.symptomIfNo);
//     symptomInput.value = chatbotState.symptoms.join(', ');
//     console.log('Added Symptom (No):', currentQuestion.symptomIfNo, 'Updated Symptoms:', chatbotState.symptoms); // Debug log
//   }

//   chatbotState.currentQuestionIndex++;
//   if (chatbotState.currentQuestionIndex < chatbotState.followUpQuestions[chatbotState.primarySymptom].length) {
//     const nextQuestion = chatbotState.followUpQuestions[chatbotState.primarySymptom][chatbotState.currentQuestionIndex].question;
//     addChatMessage(nextQuestion, 'bot');
//   } else {
//     chatbotState.step = 'more-symptoms';
//     addChatMessage('Thanks for answering! Do you have any other symptoms? (Type "no" if you’re done)', 'bot');
//   }
// }

// function handleMoreSymptoms(userInput) {
//   if (userInput.includes('no') || userInput.includes('n') || userInput.includes('nope') || userInput.includes('nah')) {
//     chatbotState.step = 'done';
//     addChatMessage(`I’ve updated the symptom input field with: ${chatbotState.symptoms.join(', ')}. I’ll now submit the form to get your recommendations. Please wait...`, 'bot');
//     console.log('Final Symptoms:', chatbotState.symptoms); // Debug log
//     // Submit the form programmatically
//     setTimeout(() => {
//       symptomForm.submit();
//     }, 1000); // Delay to allow user to read the message
//   } else {
//     const symptom = Object.keys(window.symptoms_dict).find(s => userInput.includes(s.replace('_', ' ')));
//     if (symptom) {
//       chatbotState.symptoms.push(symptom);
//       symptomInput.value = chatbotState.symptoms.join(', ');
//       console.log('Added Additional Symptom:', symptom, 'Updated Symptoms:', chatbotState.symptoms); // Debug log
//       addChatMessage(`Added ${symptom.replace('_', ' ')}. Any more symptoms? (Type "no" if you’re done)`, 'bot');
//     } else {
//       addChatMessage('I didn’t recognize that symptom. Please try again or type "no" to finish.', 'bot');
//     }
//   }
// }

// // Speech Recognition
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

// // Modal Accessibility
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

// // Handle Lab Test Form Submission
// if (labTestForm) {
//   labTestForm.addEventListener('submit', async (e) => {
//     e.preventDefault();
//     const formData = new FormData(labTestForm);
//     try {
//       const response = await fetch('/submit_test_results', {
//         method: 'POST',
//         body: formData
//       });
//       const result = await response.json();
//       if (response.ok) {
//         alert(result.message);
//         // Optionally, refresh the test history modal
//         window.location.reload(); // Reload to refresh test history
//       } else {
//         alert(result.error || 'Error saving test result');
//       }
//     } catch (error) {
//       console.error('Error submitting test result:', error);
//       alert('An error occurred while saving the test result.');
//     }
//   });
// }

// // Hospital Rendering
// function initMap() {
//   console.log("initMap called");

//   let showHospitals = false;
//   let staticHospitals = [];
//   let predictedDisease = "";

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

//   let searchTerm = 'hospitals';
//   if (window.disease.toLowerCase().includes('heart attack')) {
//     searchTerm = 'heart hospitals';
//   } else if (window.disease.toLowerCase().includes('allergy')) {
//     searchTerm = 'allergy clinics';
//   } else if (window.disease.toLowerCase().includes('diabetes')) {
//     searchTerm = 'diabetes clinics';
//   } else if (window.disease.toLowerCase().includes('asthma')) {
//     searchTerm = 'asthma specialists';
//   }
//   window.searchTerm = searchTerm;
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
//   hospitalList.innerHTML = '';
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
//     hospitalList.innerHTML = `<p>For Nearby hospitals <a href="https://www.google.com/maps/search/${encodeURIComponent(searchTerm)}" target="_blank">Click here</a>.</p>`;
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
//   initChatbot();
//   if (document.getElementById('hospital-list')) {
//     console.log("hospital-list element found, calling initMap");
//     initMap();
//   } else {
//     console.log("hospital-list element not found");
//   }
// });




// // Utility function to safely parse JSON
// function safeParseJSON(data, fallback, fieldName) {
//   try {
//     if (data === undefined || data === null || data === '' || data === '[' || data === '[]') {
//       console.warn(`safeParseJSON: Data for ${fieldName} is invalid or empty. Using fallback:`, fallback);
//       return fallback;
//     }
//     const parsed = JSON.parse(data);
//     if (!Array.isArray(parsed) && fieldName !== 'showHospitals' && fieldName !== 'predictedDisease') {
//       console.warn(`safeParseJSON: Parsed data for ${fieldName} is not an array. Using fallback:`, fallback);
//       return fallback;
//     }
//     return parsed;
//   } catch (error) {
//     console.error(`Error parsing JSON for ${fieldName}:`, error, 'Data:', data);
//     return fallback;
//   }
// }

// Element References
// const startSpeechRecognitionButton = document.getElementById('startSpeechRecognition');
// const transcriptionDiv = document.getElementById('transcription');
// const startChatbotButton = document.getElementById('startChatbot');
// const chatbotIcon = document.getElementById('chatbot-icon');
// const chatbotContainer = document.getElementById('chatbot-container');
// const chatbotClose = document.getElementById('chatbot-close');
// const chatbotBody = document.getElementById('chatbot-body');
// const chatbotInput = document.getElementById('chatbot-input');
// const chatbotSend = document.getElementById('chatbot-send');
// const symptomInput = document.getElementById('symptoms');
// const symptomForm = document.getElementById('symptom-form');
// const labTestForm = document.getElementById('lab-test-form');
// const generateReportBtn = document.getElementById('generate-report-btn');

// // Chatbot State
// let chatbotState = {
//   step: 'initial',
//   symptoms: [],
//   primarySymptom: null,
//   followUpQuestions: {
//     'chest_pain': [
//       { question: 'Does your chest pain worsen with movement?', symptomIfYes: 'movement_stiffness', symptomIfNo: null },
//       { question: 'Are you experiencing breathlessness along with chest pain?', symptomIfYes: 'breathlessness', symptomIfNo: null },
//       { question: 'Do you have a fast heart rate?', symptomIfYes: 'fast_heart_rate', symptomIfNo: null }
//     ],
//     'continuous_sneezing': [
//       { question: 'Do you have itching along with sneezing?', symptomIfYes: 'itching', symptomIfNo: null },
//       { question: 'Are you experiencing a runny nose?', symptomIfYes: 'runny_nose', symptomIfNo: null },
//       { question: 'Do you have a sore throat?', symptomIfYes: 'throat_irritation', symptomIfNo: null }
//     ],
//     'fever': [
//       { question: 'Is your fever high (above 100.4°F)?', symptomIfYes: 'high_fever', symptomIfNo: 'mild_fever' },
//       { question: 'Are you experiencing chills?', symptomIfYes: 'chills', symptomIfNo: null },
//       { question: 'Do you have a cough?', symptomIfYes: 'cough', symptomIfNo: null }
//     ],
//     'headache': [
//       { question: 'Do you feel dizzy along with your headache?', symptomIfYes: 'dizziness', symptomIfNo: null },
//       { question: 'Are you experiencing nausea?', symptomIfYes: 'nausea', symptomIfNo: null },
//       { question: 'Do you have a stiff neck?', symptomIfYes: 'stiff_neck', symptomIfNo: null }
//     ],
//     'fatigue': [
//       { question: 'Are you feeling lethargic?', symptomIfYes: 'lethargy', symptomIfNo: null },
//       { question: 'Do you have muscle weakness?', symptomIfYes: 'muscle_weakness', symptomIfNo: null },
//       { question: 'Are you experiencing weight loss?', symptomIfYes: 'weight_loss', symptomIfNo: null }
//     ],
//     'cough': [
//       { question: 'Is your cough accompanied by phlegm?', symptomIfYes: 'phlegm', symptomIfNo: null },
//       { question: 'Do you have a fever?', symptomIfYes: 'fever', symptomIfNo: null },
//       { question: 'Are you experiencing throat irritation?', symptomIfYes: 'throat_irritation', symptomIfNo: null }
//     ],
//     'vomiting': [
//       { question: 'Are you experiencing nausea?', symptomIfYes: 'nausea', symptomIfNo: null },
//       { question: 'Do you have abdominal pain?', symptomIfYes: 'abdominal_pain', symptomIfNo: null },
//       { question: 'Are you dehydrated?', symptomIfYes: 'dehydration', symptomIfNo: null }
//     ],
//   'joint_pain': [
//       { question: 'Is the joint pain worse in the morning?', symptomIfYes: 'morning_stiffness', symptomIfNo: null },
//       { question: 'Do you have swelling in the joints?', symptomIfYes: 'swelling_joints', symptomIfNo: null },
//       { question: 'Are you experiencing fatigue?', symptomIfYes: 'fatigue', symptomIfNo: null }
//     ],
//     'skin_rash': [
//       { question: 'Is the rash itchy?', symptomIfYes: 'itching', symptomIfNo: null },
//       { question: 'Do you have a fever?', symptomIfYes: 'fever', symptomIfNo: null },
//       { question: 'Is the rash spreading?', symptomIfYes: 'spreading_rash', symptomIfNo: null }
//     ],
//     'nausea': [
//       { question: 'Are you vomiting?', symptomIfYes: 'vomiting', symptomIfNo: null },
//       { question: 'Do you have abdominal pain?', symptomIfYes: 'abdominal_pain', symptomIfNo: null },
//       { question: 'Are you feeling dizzy?', symptomIfYes: 'dizziness', symptomIfNo: null }
//     ],
//     'weight_loss': [
//       { question: 'Are you experiencing fatigue?', symptomIfYes: 'fatigue', symptomIfNo: null },
//       { question: 'Do you have a loss of appetite?', symptomIfYes: 'loss_of_appetite', symptomIfNo: null },
//       { question: 'Are you having night sweats?', symptomIfYes: 'sweating', symptomIfNo: null }
//     ],
//     'abdominal_pain': [
//       { question: 'Is the pain worse after eating?', symptomIfYes: 'pain_after_eating', symptomIfNo: null },
//       { question: 'Are you experiencing nausea?', symptomIfYes: 'nausea', symptomIfNo: null },
//       { question: 'Do you have diarrhea?', symptomIfYes: 'diarrhoea', symptomIfNo: null }
//     ],
//     'dizziness': [
//       { question: 'Do you have a headache?', symptomIfYes: 'headache', symptomIfNo: null },
//       { question: 'Are you experiencing blurred vision?', symptomIfYes: 'blurred_and_distorted_vision', symptomIfNo: null },
//       { question: 'Do you feel faint?', symptomIfYes: 'fainting', symptomIfNo: null }
//     ],
//     'sweating': [
//       { question: 'Are you experiencing a fever?', symptomIfYes: 'fever', symptomIfNo: null },
//       { question: 'Do you have chest pain?', symptomIfYes: 'chest_pain', symptomIfNo: null },
//       { question: 'Are you feeling anxious?', symptomIfYes: 'anxiety', symptomIfNo: null }
//     ]
//   },
//   currentQuestionIndex: 0
// };

// // Initialize Chatbot
// function initChatbot() {
//   if (!window.symptoms_dict) {
//     console.error('window.symptoms_dict is not defined. Ensure it is passed from the server.');
//     return;
//   }

//   // Open chatbot when clicking the "Chat with Symptom Assistant" button or the icon
//   startChatbotButton.addEventListener('click', openChatbot);
//   chatbotIcon.addEventListener('click', openChatbot);
//   chatbotClose.addEventListener('click', closeChatbot);

//   // Handle sending messages
//   chatbotSend.addEventListener('click', handleChatbotInput);
//   chatbotInput.addEventListener('keypress', (e) => {
//     if (e.key === 'Enter') {
//       handleChatbotInput();
//     }
//   });

//   // Initial message
//   chatbotBody.innerHTML = '<div class="chat-message bot">Hello! I\'m here to help you describe your symptoms. What is your main symptom right now?</div>';
// }

// function openChatbot() {
//   chatbotContainer.style.display = 'flex';
//   chatbotIcon.style.display = 'none';
//   chatbotInput.focus();
// }

// function closeChatbot() {
//   chatbotContainer.style.display = 'none';
//   chatbotIcon.style.display = 'flex';
//   resetChatbot();
// }

// function resetChatbot() {
//   chatbotState = {
//     step: 'initial',
//     symptoms: [],
//     primarySymptom: null,
//     followUpQuestions: chatbotState.followUpQuestions,
//     currentQuestionIndex: 0
//   };
//   chatbotBody.innerHTML = '<div class="chat-message bot">Hello! I\'m here to help you describe your symptoms. What is your main symptom right now?</div>';
//   symptomInput.value = '';
// }

// function addChatMessage(message, sender) {
//   const messageDiv = document.createElement('div');
//   messageDiv.className = `chat-message ${sender}`;
//   messageDiv.textContent = message;
//   chatbotBody.appendChild(messageDiv);
//   chatbotBody.scrollTop = chatbotBody.scrollHeight;
// }

// function handleChatbotInput() {
//   const userInput = chatbotInput.value.trim().toLowerCase();
//   if (!userInput) return;

//   addChatMessage(userInput, 'user');
//   chatbotInput.value = '';

//   console.log('Current Step:', chatbotState.step, 'User Input:', userInput);

//   switch (chatbotState.step) {
//     case 'initial':
//       handleInitialSymptom(userInput);
//       break;
//     case 'follow-up':
//       handleFollowUpResponse(userInput);
//       break;
//     case 'more-symptoms':
//       handleMoreSymptoms(userInput);
//       break;
//     case 'done':
//       addChatMessage('I’ve already collected your symptoms. Please click "Get Recommendations" to see your results, or close this chat to start over.', 'bot');
//       break;
//   }
// }

// function handleInitialSymptom(userInput) {
//   const symptom = Object.keys(window.symptoms_dict).find(s => userInput.includes(s.replace('_', ' ')));
//   if (symptom) {
//     chatbotState.primarySymptom = symptom;
//     chatbotState.symptoms.push(symptom);
//     symptomInput.value = chatbotState.symptoms.join(', ');
//     console.log('Recognized Symptom:', symptom, 'Updated Symptoms:', chatbotState.symptoms);

//     if (chatbotState.followUpQuestions[symptom]) {
//       chatbotState.step = 'follow-up';
//       chatbotState.currentQuestionIndex = 0;
//       const question = chatbotState.followUpQuestions[symptom][0].question;
//       addChatMessage(question, 'bot');
//     } else {
//       chatbotState.step = 'more-symptoms';
//       addChatMessage(`I’ve noted ${symptom.replace('_', ' ')}. I don’t have specific follow-up questions for this symptom. Do you have any other symptoms? (Type "no" if you’re done)`, 'bot');
//     }
//   } else {
//     addChatMessage('I didn’t recognize that symptom. Please try again (e.g., chest pain, fever, headache). You can also type symptoms as they appear in the placeholder, like "chest_pain".', 'bot');
//   }
// }
// function handleFollowUpResponse(userInput) {
//   const currentQuestion = chatbotState.followUpQuestions[chatbotState.primarySymptom][chatbotState.currentQuestionIndex];
//   const isYes = userInput.includes('yes') || userInput.includes('y') || userInput.includes('yeah') || userInput.includes('yep');
//   const isNo = userInput.includes('no') || userInput.includes('n') || userInput.includes('nope') || userInput.includes('nah');

//   console.log('Follow-up Response:', userInput, 'Is Yes:', isYes, 'Is No:', isNo, 'Current Question:', currentQuestion);

//   if (!isYes && !isNo) {
//     addChatMessage('Please answer with "yes" or "no" (e.g., yes, y, no, n).', 'bot');
//     return;
//   }

//   if (isYes && currentQuestion.symptomIfYes) {
//     chatbotState.symptoms.push(currentQuestion.symptomIfYes);
//     symptomInput.value = chatbotState.symptoms.join(', ');
//     console.log('Added Symptom (Yes):', currentQuestion.symptomIfYes, 'Updated Symptoms:', chatbotState.symptoms);
//   } else if (isNo && currentQuestion.symptomIfNo) {
//     chatbotState.symptoms.push(currentQuestion.symptomIfNo);
//     symptomInput.value = chatbotState.symptoms.join(', ');
//     console.log('Added Symptom (No):', currentQuestion.symptomIfNo, 'Updated Symptoms:', chatbotState.symptoms);
//   }

//   chatbotState.currentQuestionIndex++;
//   if (chatbotState.currentQuestionIndex < chatbotState.followUpQuestions[chatbotState.primarySymptom].length) {
//     const nextQuestion = chatbotState.followUpQuestions[chatbotState.primarySymptom][chatbotState.currentQuestionIndex].question;
//     console.log('Next Follow-up Question:', nextQuestion);
//     addChatMessage(nextQuestion, 'bot');
//   } else {
//     chatbotState.step = 'more-symptoms';
//     console.log('Finished follow-up questions, transitioning to more-symptoms step');
//     addChatMessage('Thanks for answering! Do you have any other symptoms? (Type "no" if you’re done)', 'bot');
//   }
// }

// function handleMoreSymptoms(userInput) {
//   if (userInput.includes('no') || userInput.includes('n') || userInput.includes('nope') || userInput.includes('nah')) {
//     chatbotState.step = 'done';
//     addChatMessage(`I’ve updated the symptom input field with: ${chatbotState.symptoms.join(', ')}. I’ll now submit the form to get your recommendations. Please wait...`, 'bot');
//     console.log('Final Symptoms:', chatbotState.symptoms);
//     setTimeout(() => {
//       symptomForm.submit();
//     }, 1000);
//   } else {
//     const symptom = Object.keys(window.symptoms_dict).find(s => userInput.includes(s.replace('_', ' ')));
//     if (symptom) {
//       chatbotState.symptoms.push(symptom);
//       symptomInput.value = chatbotState.symptoms.join(', ');
//       console.log('Added Additional Symptom:', symptom, 'Updated Symptoms:', chatbotState.symptoms);
//       addChatMessage(`Added ${symptom.replace('_', ' ')}. Any more symptoms? (Type "no" if you’re done)`, 'bot');
//     } else {
//       addChatMessage('I didn’t recognize that symptom. Please try again or type "no" to finish.', 'bot');
//     }
//   }
// }

// // Speech Recognition Setup
// if (startSpeechRecognitionButton) {
//   const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
//   if (SpeechRecognition) {
//     const recognition = new SpeechRecognition();
//     recognition.continuous = false;
//     recognition.interimResults = false;
//     recognition.lang = 'en-US';

//     startSpeechRecognitionButton.addEventListener('click', () => {
//       recognition.start();
//       startSpeechRecognitionButton.textContent = 'Listening...';
//       startSpeechRecognitionButton.disabled = true;
//     });

//     recognition.onresult = (event) => {
//       const transcript = event.results[0][0].transcript;
//       transcriptionDiv.textContent = `You said: ${transcript}`;
//       symptomInput.value = transcript.replace(/\s+/g, ', ').toLowerCase();
//       startSpeechRecognitionButton.textContent = 'Start Speech Recognition';
//       startSpeechRecognitionButton.disabled = false;
//     };

//     recognition.onerror = (event) => {
//       console.error('Speech recognition error:', event.error);
//       transcriptionDiv.textContent = 'Error occurred in speech recognition. Please try again.';
//       startSpeechRecognitionButton.textContent = 'Start Speech Recognition';
//       startSpeechRecognitionButton.disabled = false;
//     };

//     recognition.onend = () => {
//       startSpeechRecognitionButton.textContent = 'Start Speech Recognition';
//       startSpeechRecognitionButton.disabled = false;
//     };
//   } else {
//     startSpeechRecognitionButton.disabled = true;
//     startSpeechRecognitionButton.textContent = 'Speech Recognition Not Supported';
//   }
// }

// // Modal Accessibility
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

// // Handle Health Report Generation
// if (generateReportBtn) {
//   generateReportBtn.addEventListener('click', async () => {
//     const hospitalDataElement = document.getElementById('hospital-data');
//     if (!hospitalDataElement) {
//       console.error('hospital-data element not found');
//       alert('Error: Required data element not found. Please ensure results are loaded.');
//       return;
//     }

//     console.log('Raw hospital-data attributes:', {
//       showHospitals: hospitalDataElement.dataset.showHospitals,
//       staticHospitals: hospitalDataElement.dataset.staticHospitals,
//       predictedDisease: hospitalDataElement.dataset.predictedDisease,
//       userSymptoms: hospitalDataElement.dataset.userSymptoms,
//       medications: hospitalDataElement.dataset.medications,
//       myPrecautions: hospitalDataElement.dataset.myPrecautions,
//       workout: hospitalDataElement.dataset.workout,
//       myDiet: hospitalDataElement.dataset.myDiet,
//       recommendedTests: hospitalDataElement.dataset.recommendedTests
//     });

//     const hospitalData = {
//       showHospitals: safeParseJSON(hospitalDataElement.dataset.showHospitals, false, 'showHospitals'),
//       staticHospitals: safeParseJSON(hospitalDataElement.dataset.staticHospitals, [], 'staticHospitals'),
//       predictedDisease: hospitalDataElement.dataset.predictedDisease || 'Not available',
//       userSymptoms: safeParseJSON(hospitalDataElement.dataset.userSymptoms, [], 'userSymptoms'),
//       medications: safeParseJSON(hospitalDataElement.dataset.medications, [], 'medications'),
//       myPrecautions: safeParseJSON(hospitalDataElement.dataset.myPrecautions, [], 'myPrecautions'),
//       workout: safeParseJSON(hospitalDataElement.dataset.workout, [], 'workout'),
//       myDiet: safeParseJSON(hospitalDataElement.dataset.myDiet, [], 'myDiet'),
//       recommendedTests: safeParseJSON(hospitalDataElement.dataset.recommendedTests, [], 'recommendedTests')
//     };

//     console.log('Parsed hospitalData:', hospitalData);

//     if (!hospitalData.predictedDisease || hospitalData.predictedDisease === 'Not available' || hospitalData.predictedDisease === 'null') {
//       console.warn('Predicted disease is invalid:', hospitalData.predictedDisease);
//       alert('Please submit symptoms and get a prediction before generating a report.');
//       return;
//     }

//     const reportData = {
//       symptoms: hospitalData.userSymptoms,
//       predicted_disease: hospitalData.predictedDisease,
//       description: document.querySelector('#descriptionModal .modal-body p')?.textContent || 'Not available',
//       precautions: hospitalData.myPrecautions,
//       medications: hospitalData.medications,
//       diet: hospitalData.myDiet,
//       workouts: hospitalData.workout,
//       lab_tests: hospitalData.recommendedTests
//     };

//     console.log('Report data being sent to /generate_report:', reportData);

//     try {
//       // Step 1: Call /generate_report to get the report data
//       const response = await fetch('/generate_report', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(reportData)
//       });

//       if (!response.ok) {
//         const errorText = await response.text();
//         throw new Error(`HTTP error! Status: ${response.status}, Message: ${errorText}`);
//       }

//       const result = await response.json();
//       console.log('Response from /generate_report:', result);

//       if (!result.report_data) {
//         throw new Error('No report data received from the server.');
//       }

//       // Step 2: Send the report data to /render_latex to generate PDF
//       const pdfResponse = await fetch('/render_latex', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({ report_data: result.report_data })
//       });

//       if (!pdfResponse.ok) {
//         const errorData = await pdfResponse.json();
//         throw new Error(errorData.error || 'Failed to generate PDF');
//       }

//       const blob = await pdfResponse.blob();
//       const url = window.URL.createObjectURL(blob);
//       const a = document.createElement('a');
//       a.href = url;
//       a.download = 'health_report.pdf';
//       a.click();
//       window.URL.revokeObjectURL(url);
//     } catch (error) {
//       console.error('Error generating report:', error);
//       alert('An error occurred while generating the report: ' + error.message + '. Please check the console for more details.');
//     }
//   });
// }

// // Handle Lab Test Form Submission
// if (labTestForm) {
//   labTestForm.addEventListener('submit', async (e) => {
//     e.preventDefault();
//     const formData = new FormData(labTestForm);
//     const data = {
//       disease: formData.get('disease'),
//       test_name: formData.get('test_name'),
//       test_result: formData.get('test_result'),
//       test_date: formData.get('test_date')
//     };

//     try {
//       const response = await fetch('/submit_lab_test', {
//         method: 'POST',
//         headers: {
//           'Content-Type': 'application/json'
//         },
//         body: JSON.stringify(data)
//       });

//       const result = await response.json();
//       if (response.ok) {
//         alert('Lab test result submitted successfully!');
//         window.location.reload();
//       } else {
//         throw new Error(result.error || 'Failed to submit lab test');
//       }
//     } catch (error) {
//       console.error('Error submitting lab test:', error);
//       alert('Error submitting lab test: ' + error.message);
//     }
//   });
// }

// // Hospital Rendering
// function initMap() {
//   console.log("initMap called");

//   let showHospitals = false;
//   let staticHospitals = [];
//   let predictedDisease = "";
//   let userSymptoms = [];
//   let medications = [];
//   let myPrecautions = [];
//   let workout = [];
//   let myDiet = [];
//   let recommendedTests = [];

//   const hospitalDataElement = document.getElementById('hospital-data');
//   if (hospitalDataElement) {
//     showHospitals = safeParseJSON(hospitalDataElement.dataset.showHospitals, false, 'showHospitals');
//     staticHospitals = safeParseJSON(hospitalDataElement.dataset.staticHospitals, [], 'staticHospitals');
//     predictedDisease = hospitalDataElement.dataset.predictedDisease || "";
//     userSymptoms = safeParseJSON(hospitalDataElement.dataset.userSymptoms, [], 'userSymptoms');
//     medications = safeParseJSON(hospitalDataElement.dataset.medications, [], 'medications');
//     myPrecautions = safeParseJSON(hospitalDataElement.dataset.myPrecautions, [], 'myPrecautions');
//     workout = safeParseJSON(hospitalDataElement.dataset.workout, [], 'workout');
//     myDiet = safeParseJSON(hospitalDataElement.dataset.myDiet, [], 'myDiet');
//     recommendedTests = safeParseJSON(hospitalDataElement.dataset.recommendedTests, [], 'recommendedTests');
//   } else {
//     console.error("hospital-data element not found");
//   }

//   console.log("showHospitals from hospital-data:", showHospitals);
//   console.log("staticHospitals from hospital-data:", staticHospitals);
//   console.log("predictedDisease from hospital-data:", predictedDisease);

//   window.staticHospitals = Array.isArray(staticHospitals) && staticHospitals.length > 0 ? staticHospitals : [];
//   window.disease = typeof predictedDisease === 'string' && predictedDisease ? predictedDisease : "Unknown Disease";
//   window.userSymptoms = userSymptoms;
//   window.medications = medications;
//   window.myPrecautions = myPrecautions;
//   window.workout = workout;
//   window.myDiet = myDiet;
//   window.recommendedTests = recommendedTests;

//   console.log("Static Hospitals (final):", window.staticHospitals);
//   console.log("Predicted Disease (final):", window.disease);

//   let searchTerm = 'hospitals';
//   if (window.disease.toLowerCase().includes('heart attack')) {
//     searchTerm = 'heart hospitals';
//   } else if (window.disease.toLowerCase().includes('allergy')) {
//     searchTerm = 'allergy clinics';
//   } else if (window.disease.toLowerCase().includes('diabetes')) {
//     searchTerm = 'diabetes clinics';
//   } else if (window.disease.toLowerCase().includes('asthma')) {
//     searchTerm = 'asthma specialists';
//   }
//   window.searchTerm = searchTerm;
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
//   hospitalList.innerHTML = '';
//   if (window.staticHospitals.length > 0) {
//     window.staticHospitals.forEach((hospital, index) => {
//       console.log("Rendering static hospital:", hospital);
//       const facilityCard = document.createElement('div');
//       facilityCard.className = 'hospital-card';
//       facilityCard.innerHTML = `
//         <h5>${escapeHTML(hospital.name)}</h5>
//         <p><em>Specialty: ${escapeHTML(hospital.specialty)}</em>
//                 <p>Address: ${escapeHTML(hospital.address)}</p>
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
//     hospitalList.innerHTML = `<p>For Nearby hospitals <a href="https://www.google.com/maps/search/${encodeURIComponent(searchTerm)}" target="_blank">Click here</a>.</p>`;
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
//   if (detailsDiv.style.display === 'block') {
//     detailsDiv.style.display = 'none';
//     return;
//   }
//   detailsDiv.style.display = 'block';
//   detailsDiv.innerHTML = `
//     <strong>${escapeHTML(name)}</strong><br>
//     Specialty: ${escapeHTML(specialty)}<br>
//     Address: ${escapeHTML(address)}<br>
//     Phone: ${escapeHTML(phone)}<br>
//     Website: <a href="${escapeHTML(website)}" target="_blank">${escapeHTML(website)}</a>
//   `;
// }

// // Initialize on Page Load
// document.addEventListener('DOMContentLoaded', () => {
//   initChatbot();
//   initMap();
// });
// // pres

function safeParseJSON(data, fallback, fieldName) {
  try {
    if (data === undefined || data === null || data === '' || data === '[' || data === '[]') {
      console.warn(`safeParseJSON: Data for ${fieldName} is invalid or empty. Using fallback:`, fallback);
      return fallback;
    }
    const parsed = JSON.parse(data);
    if (!Array.isArray(parsed) && fieldName !== 'showHospitals' && fieldName !== 'predictedDisease') {
      console.warn(`safeParseJSON: Parsed data for ${fieldName} is not an array. Using fallback:`, fallback);
      return fallback;
    }
    return parsed;
  } catch (error) {
    console.error(`Error parsing JSON for ${fieldName}:`, error, 'Data:', data);
    return fallback;
  }
}

// Element References
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
const labTestForm = document.getElementById('lab-test-form');
const generateReportBtn = document.getElementById('generate-report-btn');
const healthLockerForm = document.getElementById('health-locker-form');
const healthLockerTable = document.getElementById('health-locker-table');

// Chatbot State
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
    ],
    'joint_pain': [
      { question: 'Is the joint pain worse in the morning?', symptomIfYes: 'morning_stiffness', symptomIfNo: null },
      { question: 'Do you have swelling in the joints?', symptomIfYes: 'swelling_joints', symptomIfNo: null },
      { question: 'Are you experiencing fatigue?', symptomIfYes: 'fatigue', symptomIfNo: null }
    ],
    'skin_rash': [
      { question: 'Is the rash itchy?', symptomIfYes: 'itching', symptomIfNo: null },
      { question: 'Do you have a fever?', symptomIfYes: 'fever', symptomIfNo: null },
      { question: 'Is the rash spreading?', symptomIfYes: 'spreading_rash', symptomIfNo: null }
    ],
    'nausea': [
      { question: 'Are you vomiting?', symptomIfYes: 'vomiting', symptomIfNo: null },
      { question: 'Do you have abdominal pain?', symptomIfYes: 'abdominal_pain', symptomIfNo: null },
      { question: 'Are you feeling dizzy?', symptomIfYes: 'dizziness', symptomIfNo: null }
    ],
    'weight_loss': [
      { question: 'Are you experiencing fatigue?', symptomIfYes: 'fatigue', symptomIfNo: null },
      { question: 'Do you have a loss of appetite?', symptomIfYes: 'loss_of_appetite', symptomIfNo: null },
      { question: 'Are you having night sweats?', symptomIfYes: 'sweating', symptomIfNo: null }
    ],
    'abdominal_pain': [
      { question: 'Is the pain worse after eating?', symptomIfYes: 'pain_after_eating', symptomIfNo: null },
      { question: 'Are you experiencing nausea?', symptomIfYes: 'nausea', symptomIfNo: null },
      { question: 'Do you have diarrhea?', symptomIfYes: 'diarrhoea', symptomIfNo: null }
    ],
    'dizziness': [
      { question: 'Do you have a headache?', symptomIfYes: 'headache', symptomIfNo: null },
      { question: 'Are you experiencing blurred vision?', symptomIfYes: 'blurred_and_distorted_vision', symptomIfNo: null },
      { question: 'Do you feel faint?', symptomIfYes: 'fainting', symptomIfNo: null }
    ],
    'sweating': [
      { question: 'Are you experiencing a fever?', symptomIfYes: 'fever', symptomIfNo: null },
      { question: 'Do you have chest pain?', symptomIfYes: 'chest_pain', symptomIfNo: null },
      { question: 'Are you feeling anxious?', symptomIfYes: 'anxiety', symptomIfNo: null }
    ]
  },
  currentQuestionIndex: 0
};

// Initialize Chatbot
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

  // Initial message
  chatbotBody.innerHTML = '<div class="chat-message bot">Hello! I\'m here to help you describe your symptoms. What is your main symptom right now?</div>';
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

  console.log('Current Step:', chatbotState.step, 'User Input:', userInput);

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
    console.log('Recognized Symptom:', symptom, 'Updated Symptoms:', chatbotState.symptoms);

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

  console.log('Follow-up Response:', userInput, 'Is Yes:', isYes, 'Is No:', isNo, 'Current Question:', currentQuestion);

  if (!isYes && !isNo) {
    addChatMessage('Please answer with "yes" or "no" (e.g., yes, y, no, n).', 'bot');
    return;
  }

  if (isYes && currentQuestion.symptomIfYes) {
    chatbotState.symptoms.push(currentQuestion.symptomIfYes);
    symptomInput.value = chatbotState.symptoms.join(', ');
    console.log('Added Symptom (Yes):', currentQuestion.symptomIfYes, 'Updated Symptoms:', chatbotState.symptoms);
  } else if (isNo && currentQuestion.symptomIfNo) {
    chatbotState.symptoms.push(currentQuestion.symptomIfNo);
    symptomInput.value = chatbotState.symptoms.join(', ');
    console.log('Added Symptom (No):', currentQuestion.symptomIfNo, 'Updated Symptoms:', chatbotState.symptoms);
  }

  chatbotState.currentQuestionIndex++;
  if (chatbotState.currentQuestionIndex < chatbotState.followUpQuestions[chatbotState.primarySymptom].length) {
    const nextQuestion = chatbotState.followUpQuestions[chatbotState.primarySymptom][chatbotState.currentQuestionIndex].question;
    console.log('Next Follow-up Question:', nextQuestion);
    addChatMessage(nextQuestion, 'bot');
  } else {
    chatbotState.step = 'more-symptoms';
    console.log('Finished follow-up questions, transitioning to more-symptoms step');
    addChatMessage('Thanks for answering! Do you have any other symptoms? (Type "no" if you’re done)', 'bot');
  }
}

function handleMoreSymptoms(userInput) {
  if (userInput.includes('no') || userInput.includes('n') || userInput.includes('nope') || userInput.includes('nah')) {
    chatbotState.step = 'done';
    addChatMessage(`I’ve updated the symptom input field with: ${chatbotState.symptoms.join(', ')}. I’ll now submit the form to get your recommendations. Please wait...`, 'bot');
    console.log('Final Symptoms:', chatbotState.symptoms);
    setTimeout(() => {
      symptomForm.submit();
    }, 1000);
  } else {
    const symptom = Object.keys(window.symptoms_dict).find(s => userInput.includes(s.replace('_', ' ')));
    if (symptom) {
      chatbotState.symptoms.push(symptom);
      symptomInput.value = chatbotState.symptoms.join(', ');
      console.log('Added Additional Symptom:', symptom, 'Updated Symptoms:', chatbotState.symptoms);
      addChatMessage(`Added ${symptom.replace('_', ' ')}. Any more symptoms? (Type "no" if you’re done)`, 'bot');
    } else {
      addChatMessage('I didn’t recognize that symptom. Please try again or type "no" to finish.', 'bot');
    }
  }
}

// Speech Recognition Setup
if (startSpeechRecognitionButton) {
  const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
  if (SpeechRecognition) {
    const recognition = new SpeechRecognition();
    recognition.continuous = false;
    recognition.interimResults = false;
    recognition.lang = 'en-US';

    startSpeechRecognitionButton.addEventListener('click', () => {
      recognition.start();
      startSpeechRecognitionButton.textContent = 'Listening...';
      startSpeechRecognitionButton.disabled = true;
    });

    recognition.onresult = (event) => {
      const transcript = event.results[0][0].transcript;
      transcriptionDiv.textContent = `You said: ${transcript}`;
      symptomInput.value = transcript.replace(/\s+/g, ', ').toLowerCase();
      startSpeechRecognitionButton.textContent = 'Start Speech Recognition';
      startSpeechRecognitionButton.disabled = false;
    };

    recognition.onerror = (event) => {
      console.error('Speech recognition error:', event.error);
      transcriptionDiv.textContent = 'Error occurred in speech recognition. Please try again.';
      startSpeechRecognitionButton.textContent = 'Start Speech Recognition';
      startSpeechRecognitionButton.disabled = false;
    };

    recognition.onend = () => {
      startSpeechRecognitionButton.textContent = 'Start Speech Recognition';
      startSpeechRecognitionButton.disabled = false;
    };
  } else {
    startSpeechRecognitionButton.disabled = true;
    startSpeechRecognitionButton.textContent = 'Speech Recognition Not Supported';
  }
}

// Handle Health Locker Form Submission
if (healthLockerForm) {
  healthLockerForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(healthLockerForm);
    const documentType = formData.get('document_type');
    const documentFile = formData.get('document_file');

    if (!documentFile) {
      alert('Please select a file to upload.');
      return;
    }

    try {
      const response = await fetch('/upload_document', {
        method: 'POST',
        body: formData
      });

      const result = await response.json();
      if (response.ok) {
        alert('Document uploaded successfully!');
        window.location.reload();
      } else {
        throw new Error(result.error || 'Failed to upload document');
      }
    } catch (error) {
      console.error('Error uploading document:', error);
      alert('Error uploading document: ' + error.message);
    }
  });
}

// Handle Sharing Documents
document.addEventListener('click', async (e) => {
  if (e.target.classList.contains('share-btn')) {
    const docId = e.target.getAttribute('data-id');

    try {
      const response = await fetch(`/generate_share_link/${docId}`, {
        method: 'POST'
      });

      const result = await response.json();
      if (response.ok) {
        const shareUrl = result.share_url;
        const otp = result.otp;

        // Generate QR Code
        const qrCodeDiv = document.createElement('div');
        const qrCodeCanvas = document.createElement('canvas');
        qrCodeDiv.appendChild(qrCodeCanvas);

        QRCode.toCanvas(qrCodeCanvas, shareUrl, { width: 150 }, (error) => {
          if (error) {
            console.error('Error generating QR code:', error);
            alert('Failed to generate QR code.');
            return;
          }
        });

        // Create a popup to display the QR code and OTP
        const popup = document.createElement('div');
        popup.style.position = 'fixed';
        popup.style.top = '50%';
        popup.style.left = '50%';
        popup.style.transform = 'translate(-50%, -50%)';
        popup.style.background = '#fff';
        popup.style.padding = '20px';
        popup.style.borderRadius = '10px';
        popup.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.2)';
        popup.style.zIndex = '2000';
        popup.innerHTML = `
          <h5>Share Document</h5>
          <p>Scan the QR code or use the OTP to share this document:</p>
          <div id="qr-code-container"></div>
          <p><strong>OTP:</strong> ${otp}</p>
          <p><strong>Share URL:</strong> <a href="${shareUrl}" target="_blank">${shareUrl}</a></p>
          <button class="btn btn-primary" onclick="this.parentElement.remove()">Close</button>
        `;
        popup.querySelector('#qr-code-container').appendChild(qrCodeDiv);
        document.body.appendChild(popup);
      } else {
        throw new Error(result.error || 'Failed to generate share link');
      }
    } catch (error) {
      console.error('Error generating share link:', error);
      alert('Error generating share link: ' + error.message);
    }
  }
});

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

// Handle Health Report Generation
if (generateReportBtn) {
  generateReportBtn.addEventListener('click', async () => {
    const hospitalDataElement = document.getElementById('hospital-data');
    if (!hospitalDataElement) {
      console.error('hospital-data element not found');
      alert('Error: Required data element not found. Please ensure results are loaded.');
      return;
    }

    console.log('Raw hospital-data attributes:', {
      showHospitals: hospitalDataElement.dataset.showHospitals,
      staticHospitals: hospitalDataElement.dataset.staticHospitals,
      predictedDisease: hospitalDataElement.dataset.predictedDisease,
      userSymptoms: hospitalDataElement.dataset.userSymptoms,
      medications: hospitalDataElement.dataset.medications,
      myPrecautions: hospitalDataElement.dataset.myPrecautions,
      workout: hospitalDataElement.dataset.workout,
      myDiet: hospitalDataElement.dataset.myDiet,
      recommendedTests: hospitalDataElement.dataset.recommendedTests
    });

    const hospitalData = {
      showHospitals: safeParseJSON(hospitalDataElement.dataset.showHospitals, false, 'showHospitals'),
      staticHospitals: safeParseJSON(hospitalDataElement.dataset.staticHospitals, [], 'staticHospitals'),
      predictedDisease: hospitalDataElement.dataset.predictedDisease || 'Not available',
      userSymptoms: safeParseJSON(hospitalDataElement.dataset.userSymptoms, [], 'userSymptoms'),
      medications: safeParseJSON(hospitalDataElement.dataset.medications, [], 'medications'),
      myPrecautions: safeParseJSON(hospitalDataElement.dataset.myPrecautions, [], 'myPrecautions'),
      workout: safeParseJSON(hospitalDataElement.dataset.workout, [], 'workout'),
      myDiet: safeParseJSON(hospitalDataElement.dataset.myDiet, [], 'myDiet'),
      recommendedTests: safeParseJSON(hospitalDataElement.dataset.recommendedTests, [], 'recommendedTests')
    };

    console.log('Parsed hospitalData:', hospitalData);

    if (!hospitalData.predictedDisease || hospitalData.predictedDisease === 'Not available' || hospitalData.predictedDisease === 'null') {
      console.warn('Predicted disease is invalid:', hospitalData.predictedDisease);
      alert('Please submit symptoms and get a prediction before generating a report.');
      return;
    }

    const reportData = {
      symptoms: hospitalData.userSymptoms,
      predicted_disease: hospitalData.predictedDisease,
      description: document.querySelector('#descriptionModal .modal-body p')?.textContent || 'Not available',
      precautions: hospitalData.myPrecautions,
      medications: hospitalData.medications,
      diet: hospitalData.myDiet,
      workouts: hospitalData.workout,
      lab_tests: hospitalData.recommendedTests
    };

    console.log('Report data being sent to /generate_report:', reportData);

    try {
      // Step 1: Call /generate_report to get the report data
      const response = await fetch('/generate_report', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(reportData)
      });

      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`HTTP error! Status: ${response.status}, Message: ${errorText}`);
      }

      const result = await response.json();
      console.log('Response from /generate_report:', result);

      if (!result.report_data) {
        throw new Error('No report data received from the server.');
      }

      // Step 2: Send the report data to /render_latex to generate PDF
      const pdfResponse = await fetch('/render_latex', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ report_data: result.report_data })
      });

      if (!pdfResponse.ok) {
        const errorData = await pdfResponse.json();
        throw new Error(errorData.error || 'Failed to generate PDF');
      }

      const blob = await pdfResponse.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'health_report.pdf';
      a.click();
      window.URL.revokeObjectURL(url);
    } catch (error) {
      console.error('Error generating report:', error);
      alert('An error occurred while generating the report: ' + error.message + '. Please check the console for more details.');
    }
  });
}

// Handle Lab Test Form Submission
if (labTestForm) {
  labTestForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(labTestForm);
    const data = {
      disease: formData.get('disease'),
      test_name: formData.get('test_name'),
      test_result: formData.get('test_result'),
      test_date: formData.get('test_date')
    };

    try {
      const response = await fetch('/submit_lab_test', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
      });

      const result = await response.json();
      if (response.ok) {
        alert('Lab test result submitted successfully!');
        window.location.reload();
      } else {
        throw new Error(result.error || 'Failed to submit lab test');
      }
    } catch (error) {
      console.error('Error submitting lab test:', error);
      alert('Error submitting lab test: ' + error.message);
    }
  });
}

// Hospital Rendering
function initMap() {
  console.log("initMap called");

  let showHospitals = false;
  let staticHospitals = [];
  let predictedDisease = "";
  let userSymptoms = [];
  let medications = [];
  let myPrecautions = [];
  let workout = [];
  let myDiet = [];
  let recommendedTests = [];

  const hospitalDataElement = document.getElementById('hospital-data');
  if (hospitalDataElement) {
    showHospitals = safeParseJSON(hospitalDataElement.dataset.showHospitals, false, 'showHospitals');
    staticHospitals = safeParseJSON(hospitalDataElement.dataset.staticHospitals, [], 'staticHospitals');
    predictedDisease = hospitalDataElement.dataset.predictedDisease || "";
    userSymptoms = safeParseJSON(hospitalDataElement.dataset.userSymptoms, [], 'userSymptoms');
    medications = safeParseJSON(hospitalDataElement.dataset.medications, [], 'medications');
    myPrecautions = safeParseJSON(hospitalDataElement.dataset.myPrecautions, [], 'myPrecautions');
    workout = safeParseJSON(hospitalDataElement.dataset.workout, [], 'workout');
    myDiet = safeParseJSON(hospitalDataElement.dataset.myDiet, [], 'myDiet');
    recommendedTests = safeParseJSON(hospitalDataElement.dataset.recommendedTests, [], 'recommendedTests');
  } else {
    console.error("hospital-data element not found");
  }

  console.log("showHospitals from hospital-data:", showHospitals);
  console.log("staticHospitals from hospital-data:", staticHospitals);
  console.log("predictedDisease from hospital-data:", predictedDisease);

  window.staticHospitals = Array.isArray(staticHospitals) && staticHospitals.length > 0 ? staticHospitals : [];
  window.disease = typeof predictedDisease === 'string' && predictedDisease ? predictedDisease : "Unknown Disease";
  window.userSymptoms = userSymptoms;
  window.medications = medications;
  window.myPrecautions = myPrecautions;
  window.workout = workout;
  window.myDiet = myDiet;
  window.recommendedTests = recommendedTests;

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
        <p><em>Specialty: ${escapeHTML(hospital.specialty)}</em>
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
  if (detailsDiv.style.display === 'block') {
    detailsDiv.style.display = 'none';
    return;
  }
  detailsDiv.style.display = 'block';
  detailsDiv.innerHTML = `
    <strong>${escapeHTML(name)}</strong><br>
    Specialty: ${escapeHTML(specialty)}<br>
    Address: ${escapeHTML(address)}<br>
    Phone: ${escapeHTML(phone)}<br>
    Website: <a href="${escapeHTML(website)}" target="_blank">${escapeHTML(website)}</a>
  `;
}

// Initialize on Page Load
document.addEventListener('DOMContentLoaded', () => {
  initChatbot();
  initMap();
});