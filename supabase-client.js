import { createClient } from 'https://cdn.jsdelivr.net/npm/@supabase/supabase-js/+esm'

const supabaseUrl = 'https://sjywjholwoybhwrrdahw.supabase.co'
const supabaseKey = 'sb_publishable_OrlFuoUqR6IoUpwofKTDWQ_TixE8b1g'

export const supabase = createClient(supabaseUrl, supabaseKey)

// Make it available globally so other inline scripts can use it if needed
window.supabase = supabase;
console.log("Supabase connected successfully!");
