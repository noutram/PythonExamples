///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "MyProjectBase.h"

///////////////////////////////////////////////////////////////////////////

MainDialog::MainDialog( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxDialog( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );

	wxBoxSizer* verticalSizer;
	verticalSizer = new wxBoxSizer( wxVERTICAL );

	btnOk = new wxButton( this, wxID_ANY, _("OK"), wxDefaultPosition, wxDefaultSize, 0 );
	btnOk->SetMinSize( wxSize( 100,-1 ) );

	verticalSizer->Add( btnOk, 0, wxALIGN_CENTER_HORIZONTAL|wxALL, 5 );

	btnSave = new wxButton( this, wxID_ANY, _("Save"), wxDefaultPosition, wxDefaultSize, 0 );
	btnSave->SetToolTip( _("Click this to edit") );
	btnSave->SetMinSize( wxSize( 100,-1 ) );

	verticalSizer->Add( btnSave, 0, wxALIGN_CENTER_HORIZONTAL|wxALL, 5 );

	txtEdit = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	txtEdit->SetMinSize( wxSize( 300,-1 ) );

	verticalSizer->Add( txtEdit, 1, wxALIGN_CENTER_HORIZONTAL|wxALL|wxEXPAND, 5 );

	lblMessage = new wxStaticText( this, wxID_ANY, _("Enter notes"), wxDefaultPosition, wxDefaultSize, 0 );
	lblMessage->Wrap( -1 );
	verticalSizer->Add( lblMessage, 0, wxALL|wxALIGN_CENTER_HORIZONTAL, 5 );


	this->SetSizer( verticalSizer );
	this->Layout();

	this->Centre( wxBOTH );

	// Connect Events
	btnOk->Connect( wxEVT_LEFT_DOWN, wxMouseEventHandler( MainDialog::onOkClicked ), NULL, this );
	btnSave->Connect( wxEVT_LEFT_DOWN, wxMouseEventHandler( MainDialog::onEditClicked ), NULL, this );
}

MainDialog::~MainDialog()
{
}
