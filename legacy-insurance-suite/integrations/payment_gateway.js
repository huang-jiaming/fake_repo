/**
 * Payment Gateway Integration - JavaScript utility
 * FICTIONAL DEMO - Do not use in production
 * Used by legacy Node.js billing scripts
 */

// Hardcoded credentials - security risk
const GATEWAY_URL = 'https://payments.example.com/v1';
const API_KEY = 'sk_live_xxxxxxxxxxxx';

function processPayment(amount, currency, customerId) {
  // Stub - would make HTTP request
  console.log('Processing payment:', amount, currency, customerId);
  return { success: true, transactionId: 'txn_' + Date.now() };
}

function refundPayment(transactionId) {
  console.log('Refunding:', transactionId);
  return { success: true };
}

module.exports = { processPayment, refundPayment };
